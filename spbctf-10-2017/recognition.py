from PIL import Image
import requests
def recognize(period, length, sequence):
	offsets = period + 1, period, period - 1, 1, -1, -period + 1, -period, -period - 1
	count = 0
	for index in range(length):
		if not sequence[index]:
			continue
		state = 0
		for offset in offsets:
			if 0 <= index + offset < length and sequence[index + offset] and 0 <= index % period + (offset + 1) % period - 1 < period:
				if state:
					break
				state = 1
		else:
			count += 2 - state
	return count
if __name__ == '__main__':
	cookies = dict(PHPSESSID='4bhq1brgmrml2acmj6nbtghch0')
	# for i in range(999):
	while True:
		count = 0
		major = 0
		while True:
			with Image.open(requests.get('https://linetcha.spb.ctf.su/?cpt', cookies=cookies, stream=True).raw) as image:
				period = image.width
				length = image.height * period
				sequence = image.convert('P', palette=Image.ADAPTIVE).getdata()
			guess = (recognize(period, length, sequence) + 1) // 2
			major = max(major, guess)
			# print('  {:2} {:2}'.format(major, guess))
			if major < count * 2 or major is 10:
				# print('{:1} {:2}'.format(count, major))
				break
			count += 1
		requests.post('https://linetcha.spb.ctf.su/', cookies=cookies, data=dict(guess=major))
