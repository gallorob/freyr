from dungeon_despair.domain.level import Level


class TestCase:
	def __init__(self,
	             fname: str):
		with open(fname, 'r') as f:
			self.queries = f.readlines()
		self.step = 0
		self.use_case = int(fname[-1])
	
	@property
	def tot_steps(self):
		return len(self.queries)
	
	def get_query(self) -> str:
		query = self.queries[self.step]
		self.step += 1
		return query
	
	def get_level(self,
	              step: int = 1) -> Level:
		if step == 1:
			fname = './resources/levels/empty.bin'
		else:
			fname = f'./resources/levels/{self.use_case}/{step}.bin'
		return Level.load_from_file(fname)[0]
