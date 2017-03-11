import base64
import os
import sys
if __name__ == '__main__':
	if 2 == len(sys.argv):
		string = sys.argv[1]
		print('/7779317', base64.b64encode(string.encode()).decode())
		print('<', eval(string), '>')
