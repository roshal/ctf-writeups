import os
sequence = [6, 26, 0, 13, 26, 1]
for symbol in 'abcdefghijklmnopqrstuvwxyz':
	for i, value in enumerate(map(int, os.popen('echo ' + symbol * 6 + ' | cry200.exe').read().split())):
		if sequence[i] == value:
			sequence[i] = symbol
print(''.join(sequence))
