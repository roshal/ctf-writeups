import os
def work(integer, couples):
	for couple in couples:
		if integer % couple[0] != couple[1]:
			return False
	return True
def worker(a, b, c):
	integer = 0
	for number in c, b, a:
		integer <<= 8
		integer += number
	couples = (3571, 2963), (2843, 215), (30243, 13059)
	if work(integer, couples):
		print('a', a, b, c)
	couples = (80735, 51964), (8681, 2552), (40624, 30931)
	if work(integer, couples):
		print('b', a, b, c)
	couples = (99892, 92228), (45629, 1080), (24497, 12651)
	if work(integer, couples):
		print('c', a, b, c)
	couples = (54750, 26981), (99627, 79040), (84339, 77510)
	if work(integer, couples):
		print('d', a, b, c)
if __name__ == '__main__':
	try:
		for a in range(256):
			print('>', a)
			for b in range(256):
				for c in range(256):
					worker(a, b, c)
	except KeyboardInterrupt:
		os._exit(0)
