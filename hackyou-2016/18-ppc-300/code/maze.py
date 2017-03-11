class maze():
	def __init__(self, items, width, source, destination):
		self.items = items
		self.width = width
		self.source = source
		self.destination = destination
		self.offsets = (-1, -self.width, 1, self.width)
	def getBlindPath(self, *, display = False, reverse = False):
		index = self.source
		last = 0
		items = [index]
		if self.items and self.offsets:
			while index != self.destination:
				if display:
					print(self.getView(items))
				variants = [self.items[index + offset] for offset in self.offsets]
				last = maze.getStep(last, variants, reverse = reverse)
				index += self.offsets[last]
				items.append(index)
		return items
	def getStep(last, variants, *, reverse = False):
		items = list(enumerate(variants))
		if reverse:
			items.reverse()
			last *= -1
			last -= 1
		last -= 1
		last %= len(variants)
		items = items[last:] + items[:last]
		for index, value in items:
			if value:
				return index
	def getPath(self, *, display = False, reverse = False, shortest = False):
		nodes = []
		items = [self.source]
		def tree(index):
			nonlocal nodes
			if index in nodes:
				return []
			nodes.append(index)
			if index == self.destination:
				return []
			branches = []
			if display:
				print(self.getView(nodes))
			offsets = list(self.offsets)
			if reverse:
				offsets.reverse()
			for offset in offsets:
				i = index + offset
				if self.items[i]:
					branch = [i] + tree(i)
					if shortest:
						branches.append(branch)
					elif self.destination in branch:
						return branch
			if shortest:
				for branch in sorted(branches):
					if self.destination in branch:
						return branch
			return []
		if self.items:
			items += tree(self.source)
		return items
	def getSteps(self, path = None):
		if not path:
			path = self.getPath()
		offsets = list(self.offsets)
		items = []
		if path:
			last = path[0]
			for item in path[1:]:
				items.append(offsets.index(item - last))
				last = item
		return items
	def getView(self, indexes, *, cells = [item * 2 for item in '\u2591\u2592\u2593']):
		items = []
		for index, value in enumerate(self.items):
			if not index % self.width and index:
				items.append('\n')
			if index in indexes:
				symbol = cells[2]
			else:
				if value:
					symbol = cells[0]
				else:
					symbol = cells[1]
			items.append(symbol)
		return ''.join(items)
	def getViews(self, items):
		items = []
		for item in items:
			items.append(self.getView(item))
		return items
if __name__ == '__main__':
	try:
		width = 41
		destination = width * 2 - 2
		match = '''
+---+-+-------+-+-----+-+-+------------  
|   | |       | |     | | |              
| --+ | ------+ | ----+ | | --------+ | |
|                     |   |         | | |
| --+ | | +-+ | | | +-+ --+ ----+ --+-+-+
|   | | | | | | | | |           |   | | |
| --+-+ +-+ +-+-+-+-+ ----+ ----+-+-+ | |
|   | | |         | |     |       | | | |
| --+ +-+ --+ | --+ | ----+---+---+ | | |
|   |   |   | |           |   |   | |   |
| --+ --+ --+-+ | | | ----+ +-+ --+ | --+
|             | | | |     | | |         |
| | | | | --+-+-+-+-+ --+-+ | | ----+ | |
| | | | |   | |   |     | |         | | |
| | +-+-+ --+ | --+-+ --+ | ----+ --+-+-+
| |   |             |           |   |   |
+-+ --+-+ | | | ----+ | | | ----+---+ --+
|       | | | |     | | | |             |
+-- ----+-+-+ +-+ --+ | +-+ | ------+ --+
|O        |     |   | | |   |       |   |
+---------+-----+---+-+-+---+-------+---+
'''
		sequence = tuple(symbol for symbol in match if symbol not in '\r\n')
		source = sequence.index('O')
		sequence = tuple(symbol in ' O' for symbol in sequence)
		labyrinth = maze(sequence, width, source, destination)
		path = labyrinth.getBlindPath()
		steps = labyrinth.getSteps(path)
		print(labyrinth.getView(path))
		print(path)
		print(steps)
		path = labyrinth.getPath()
		steps = labyrinth.getSteps(path)
		print(labyrinth.getView(path))
		print(path)
		print(steps)
	except KeyboardInterrupt:
		os._exit(0)
