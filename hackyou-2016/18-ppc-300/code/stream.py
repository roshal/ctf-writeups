import socket
class stream():
	def __init__(self, addres, port, *, timeout = 1):
		self.host = addres, port
		self.get_count = 0
		self.put_count = 0
		self.socket = socket.socket()
		self.socket.settimeout(timeout)
	def open(self):
		self.socket.connect(self.host)
	def close(self):
		self.socket.close()
	def get(self, *, display = False, length = 1024):
		self.get_count += 1
		sequence = []
		while True:
			try:
				raw = self.socket.recv(length)
			except socket.timeout:
				break
			if not raw:
				break
			sequence.append(raw.decode())
		string = ''.join(sequence)
		if display:
			print('<', self.get_count)
			print(string)
		return string
	def put(self, string, *, display = False):
		self.put_count += 1
		self.socket.send(string.encode())
		if display:
			print('>', self.put_count)
			print(string)
		return string
