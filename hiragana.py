# vokale
vowels = "aiueo"

# for-schleife
# jedes character des string (deswegen c in s) wird einzeln betrachtet
# result ist der speicher, hier werden die konvertierten zeichen gespeichert
def converter(string):
	# speicher
	result = ''

	# das hier ist eine sogenannte Flagge
	# sie wird genau dann True gesetzt, wenn wir eine Iteration überspringen wollen
	# sie wird anfangs auf False gesetzt, damit sie nicht gleich etwas bewirkt
	skip = False

	# erster for-loop
	for char1 in string:

		# hier wird entschieden, ob diese Iteration überspringen wird (continue bewirkt das)
		# falls True, dann muss man sie natürlich wieder False setzen, sonst überspringt den ganzen rest des wortes
		if skip:
			skip = False 
			continue
		
		# k-reihe
		if char1 == 'k':
			
			# zweiter for-loop um vokale zu vergleichen
			for char2 in vowels:		
				
				if char2 == 'a': 
					result = result + 'か'
					# hier True setzen, weil der 2te for-loop den zweiten buchstaben schon betrachtet!
					skip = True

				# TODO: vervollständigen

		# TODO: s-reihe hinzufügen

		if   char1 == 'a': result = result + 'あ'
		elif char1 == 'i': result = result + 'い'
		elif char1 == 'u': result = result + 'う'
		elif char1 == 'e': result = result + 'え'
		elif char1 == 'o': result = result + 'お'
		
		elif char1 == 'n': result = result + 'ん'

	# nach dem for-loop soll das ergebnis ausgegeben werden
	print(result)

# test-wort
test = "akaa"

# hier wird die funktion mit der eingabe des test-wortes aufgerufen
converter(test)

# "kaa"  -> "かあ""
# "akaa" -> "あかあ"
