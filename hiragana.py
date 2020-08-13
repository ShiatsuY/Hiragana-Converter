test = "aeiou"

def converter(s):
	result = ''

	for c in s:
		if   c == 'a': result = result + 'あ'
		elif c == 'e': result = result + 'え'
		elif c == 'i': result = result + 'い'
		elif c == 'o': result = result + 'お'
		elif c == 'u': result = result + 'う'

	print(result)

converter(test)