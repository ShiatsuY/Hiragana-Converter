# test-wort zum übersetzen
test = "aeiou"

# for-schleife
# jedes character des string (deswegen c in s) wird einzeln betrachtet
# result ist der speicher, hier werden die konvertierten zeichen gespeichert
def converter(s):
	# speicher
	result = ''

	# for-schleife
	for c in s:
		if   c == 'a': result = result + 'あ'
		elif c == 'e': result = result + 'え'
		elif c == 'i': result = result + 'い'
		elif c == 'o': result = result + 'お'
		elif c == 'u': result = result + 'う'

	# nach der for-schleife soll das ergebnis ausgegeben werden
	print(result)

# hier wird die funktion mit der eingabe des test-wortes aufgerufen
converter(test)