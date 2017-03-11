from maze import maze
from stream import stream
import os
import re
if __name__ == '__main__':
	try:
		global stream
		stream = stream('hackyou-ppc300.ctf.su', 11111, timeout = 1 / 4)
		stream.open()
		count = 0
		width = 41
		destination = width * 2 - 2
		while True:
			count += 1
			text = stream.get()
			if not text:
				break
			print(count)
			print('/')
			print(text[:1337])
			print('/')
			print('...')
			print('...')
			print('/')
			print(text[-1337:])
			print('/')
			matches = re.findall('\+.+O.+\+', text[-905:], re.DOTALL)
			if matches:
				match = matches[0]
				items = tuple(symbol for symbol in match if symbol not in '\r\n')
				source = items.index('O')
				items = tuple(symbol in ' O' for symbol in items)
				labyrinth = maze(items, width, source, destination)
				path = labyrinth.getPath()
				steps = labyrinth.getSteps(path)
				print(labyrinth.getView(path))
				string = ''.join('awds'[index] for index in steps)
				stream.put(string)
		stream.close()
	except KeyboardInterrupt:
		os._exit(0)
