from datetime import datetime
import os


class CustomLogger:
	def __init__(self):
		self.dir_name = None
		self.expname = None
	
	def set_dirname(self,
	                dir_name: str) -> None:
		self.dir_name = dir_name
		os.makedirs(f'./experiments/{self.dir_name}', exist_ok=True)
	
	def start_exp(self,
	              expname: str) -> None:
		self.expname = expname
		self.write_msg(source='self',
		               msg='START OF EXPERIMENT')
	
	def end_exp(self) -> None:
		self.write_msg(source='self',
		               msg='END OF EXPERIMENT')
		self.expname = None
	
	def write_msg(self,
	              source: str,
	              msg: str) -> None:
		timestamp = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
		with open(f'./experiments/{self.dir_name}/{self.expname}.log', 'a') as f:
			f.write(f'[{timestamp}] {source} - {msg}\n')


custom_logger = CustomLogger()
