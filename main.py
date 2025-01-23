from datetime import datetime
from timeit import default_timer
from typing import Union

import fire
import pandas as pd
from ollama import ResponseError
from tqdm.auto import tqdm, trange

from configs import config
from freyr_llm import LLMsCache, FreyrLLM
from logger import custom_logger
from tests import TestCase
from tool_llm import ToolCallingLLM
from freyr_outlines_llm import FreyrOutlinesLLM, OutlinesLLMsCache
from validators import validate_level_design, validate_level_domain, validate_intents

llms = [
	'llama3.1',
	'qwen2.5',
	'gemma2',
	'gemma2:27b',
	'command-r'
]
tcases = [
	'test_cases/test_case_1',
	'test_cases/test_case_2',
	'test_cases/test_case_3',
	'test_cases/test_case_4',
	'test_cases/test_case_5'
]
other_llm = 'qwen2.5:0.5b'
n_runs = 10

base_rng_seed = config.rng_seed

model_to_hf_repo = {
	'llama3.1': 'meta-llama/Llama-3.1-8B',
	'qwen2.5': 'Qwen/Qwen2.5-7B',
	'qwen2.5:0.5b': 'Qwen/Qwen2.5-0.5B',
	'gemma2': 'google/gemma-2-9b',
	'gemma2:27b': 'google/gemma-2-27b',
	'command-r': 'CohereForAI/c4ai-command-r-v01',
}


def run_test_case(llm: Union[FreyrLLM, ToolCallingLLM],
                  tcase: TestCase,
                  use_bootstrap: bool,
                  results_df: pd.DataFrame,
                  **kwargs):
	level = tcase.get_level()
	conversation_history = []
	with trange(tcase.tot_steps, desc='Test Steps', dynamic_ncols=True, leave=False) as pbar:
		while tcase.step < tcase.tot_steps:
			q = tcase.get_query().strip()
			custom_logger.write_msg(source='main',
			                        msg=f'step={tcase.step}; query={q}')
			try:
				if use_bootstrap:
					level = tcase.get_level(tcase.step)
				old_level = level.model_copy(deep=True)
				start = default_timer()
				llm_response = llm(user_message=q,
				                   conversation_history=conversation_history,
				                   level=level)
				end = default_timer()
				success = True
			except (ValueError, KeyError, TypeError) as e:
				end = default_timer()
				success = False
				custom_logger.write_msg(source='main',
				                        msg=f'Exception: {e} ({type(e)})')
			
			if success:
				if hasattr(llm, 'intents'):
					try:
						expected_intents = validate_intents(use_case=tcase.use_case,
						                                    step=tcase.step - 1,
						                                    intents=llm.intents)
						custom_logger.write_msg(source='main',
						                        msg=f'{expected_intents=}')
					except Exception as e:
						custom_logger.write_msg(source='main.validate_intents',
						                        msg=f'Exception: {e} ({type(e)})')
						expected_intents = False
				else:
					expected_intents = False
				try:
					valid_domain = validate_level_domain(use_case=tcase.use_case,
					                                     step=tcase.step - 1,
					                                     old_level=old_level,
					                                     new_level=level)
					custom_logger.write_msg(source='main',
					                        msg=f'{valid_domain=}')
				except Exception as e:
					custom_logger.write_msg(source='main.validate_level_domain',
					                        msg=f'Exception: {e} ({type(e)})')
					valid_domain = False
				if valid_domain:
					try:
						valid_design = validate_level_design(use_case=tcase.use_case,
						                                     step=tcase.step - 1,
						                                     old_level=old_level,
						                                     new_level=level)
						custom_logger.write_msg(source='main',
						                        msg=f'{valid_design=}')
					except Exception as e:
						custom_logger.write_msg(source='main.validate_level_design',
						                        msg=f'Exception: {e} ({type(e)})')
						valid_design = False
				else:
					valid_design = False
					custom_logger.write_msg(source='main',
					                        msg=f'{valid_design=}')
				conversation_history.append(q)
				conversation_history.append(llm_response)
				pbar.update(1)
			else:
				expected_intents = False
				valid_domain = False
				valid_design = False
				llm_response = ''
			
			step_results = {
				'intent_llm': kwargs.get('intent_llm', 'UNK'),
				'params_llm': kwargs.get('params_llm', 'N/A'),
				'summary_llm': other_llm,
				'chat_llm': other_llm,
				'run_n': kwargs.get('run_n', -1),
				'logfile': kwargs.get('timestamp', 'N/A'),
				'seed': config.rng_seed,
				'test_case': tcase.use_case,
				'step': tcase.step,
				'query': q,
				'success': success,
				'level': level.model_dump_json(),
				'response': llm_response,
				'expected_intents': expected_intents,
				'valid_domain': valid_domain,
				'valid_design': valid_design,
				'elapsed_time': end - start
			}
			results_df = pd.concat([pd.DataFrame(step_results, index=[0]), results_df], ignore_index=True)
			results_df.to_csv(f'./experiments/{custom_logger.dir_name}/summary_results.csv', index=False)
			
			if not valid_domain and not use_bootstrap:
				break
	return results_df


def run_experiment(msg: str,
                   dirname: str,
                   freyr_mode: bool,
                   bootstrap_mode: bool,
                   outlines_mode: bool = False) -> None:
	summary_results = pd.DataFrame()
	
	if freyr_mode:
		llmcache = LLMsCache() if not outlines_mode else OutlinesLLMsCache()
		llmcache.try_add_model(role='summary', model_name=other_llm if not outlines_mode else model_to_hf_repo[other_llm])
		llmcache.try_add_model(role='chat', model_name=other_llm if not outlines_mode else model_to_hf_repo[other_llm])
		
		with tqdm(llms, desc='Intent LLMs', dynamic_ncols=True, leave=False) as intent_pbar:
			with tqdm(llms, 'Param LLMs', dynamic_ncols=True, leave=False) as params_pbar:
				for intent_llm in intent_pbar:
					intent_pbar.set_description(f'Intent LLM {intent_llm}')
					if llmcache.role_has_model(role='intent'): llmcache.drop_model_by_role(role='intent')
					llmcache.try_add_model(role='intent', model_name=intent_llm if not outlines_mode else model_to_hf_repo[intent_llm])
					for params_llm in params_pbar:
						if llmcache.role_has_model(role='params'): llmcache.drop_model_by_role(role='params')
						params_pbar.set_description(f'Param LLM {params_llm}')
						llmcache.try_add_model(role='params', model_name=params_llm if not outlines_mode else model_to_hf_repo[params_llm])
						for run_n in trange(n_runs, desc='Runs', dynamic_ncols=True, leave=False):
							for tcase in tqdm(tcases, desc='Test cases', dynamic_ncols=True, leave=False):
								config.rng_seed = base_rng_seed + (run_n * 5)
								llm = FreyrLLM(cache=llmcache) if not outlines_mode else FreyrOutlinesLLM(cache=llmcache)
								timestamp = f'{datetime.now():%Y%m%d%H%M%S%z}'
								testcase = TestCase(fname=tcase)
								custom_logger.set_dirname(dirname)
								custom_logger.start_exp(timestamp)
								custom_logger.write_msg(source='main.config',
								                        msg=f'config={str(config.__dict__)}')
								custom_logger.write_msg(source='main.run_msg',
								                        msg=f'run={msg}')
								custom_logger.write_msg(source='main',
								                        msg=f'Start of Test Case {testcase.use_case} (run={run_n})')
								custom_logger.write_msg(source='main',
								                        msg=f'{intent_llm=}; {params_llm=}')
								
								summary_results = run_test_case(llm=llm,
								                                tcase=testcase,
								                                use_bootstrap=bootstrap_mode,
								                                results_df=summary_results,
								                                **{'run_n': run_n,
								                                   'timestamp': timestamp,
								                                   'intent_llm': intent_llm,
								                                   'params_llm': params_llm})
								
								custom_logger.end_exp()
						
						llmcache.drop_model_by_role(role='params')
					llmcache.drop_model_by_role(role='intent')
	
	else:
		with tqdm(llms, desc='LLMs', dynamic_ncols=True, leave=False) as llm_pbar:
			for model_name in llm_pbar:
				llm_pbar.set_description(f'LLM {model_name}')
				try:
					for run_n in trange(n_runs, desc='Runs', dynamic_ncols=True, leave=False):
						config.rng_seed = base_rng_seed + (run_n * 5)
						for tcase in tqdm(tcases, desc='Test cases', dynamic_ncols=True, leave=False):
							config.rng_seed = base_rng_seed + (run_n * 5)
							llm = ToolCallingLLM(model_name=model_name)
							timestamp = f'{datetime.now():%Y%m%d%H%M%S%z}'
							testcase = TestCase(fname=tcase)
							custom_logger.set_dirname(dirname)
							custom_logger.start_exp(timestamp)
							custom_logger.write_msg(source='main.config',
							                        msg=f'config={str(config.__dict__)}')
							custom_logger.write_msg(source='main.run_msg',
							                        msg=f'run={msg}')
							custom_logger.write_msg(source='main',
							                        msg=f'Start of Test Case {testcase.use_case} (run={run_n})')
							custom_logger.write_msg(source='main',
							                        msg=f'{model_name=}')
							
							summary_results = run_test_case(llm=llm,
							                                tcase=testcase,
							                                use_bootstrap=bootstrap_mode,
							                                results_df=summary_results,
							                                **{'run_n': run_n,
							                                   'timestamp': timestamp,
							                                   'intent_llm': model_name})
							
							custom_logger.end_exp()
				except ResponseError as e:
					print(f'Skipped {model_name} as it does not support tools. - {e}')
					pass


if __name__ == '__main__':
	fire.Fire(run_experiment)
