# for-schleife
# jeder buchstabe des wortes wird einzeln betrachtet
# result ist der speicher, hier werden die konvertierten zeichen gespeichert
def converter(wort):
	# speicher
	result = ''

	# das hier ist eine sogenannte Flagge
	# sie wird genau dann True gesetzt, wenn wir eine Iteration überspringen wollen
	# sie wird anfangs auf False gesetzt, damit sie nicht gleich etwas bewirkt
	skip = False

	# erster for-loop
	# pos steht für position, das ist unser zähler, er gibt uns die position wo wir bei unserem wort sind
	# beispiel 
	# sei pos = 2 und wort "abc"
	# dann ist wort[2] = 'b', weil 'b' der zweite buchstabe ist
	# wir durchlaufen jetzt also unser wort mit einem zähler und geben uns mit wort[pos] den buchstaben aus
	# range gibt ein intervall an
	# es startet bei 1 und geht bis zu unserem angegeben wert
	# len steht für length, also wenn wort = "abc" ist, dann ist len(wort) = 3
	# folglich ist range(len(wort)) = (1, 3)
	# pos kann also 1,2 oder 3 werden
	for pos in range(len(wort)):

		# hier wird entschieden, ob diese Iteration überspringen wird (continue bewirkt das)
		# falls True, dann muss man sie natürlich wieder False setzen, sonst überspringt den ganzen rest des wortes
		if skip:
			skip = False 
			continue 
		
		# k-reihe
		if wort[pos] == 'k':

			# um den nächsten buchstaben schon zu betrachten benutzen wir einen kleinen trick:
			# wir addieren eine 1 auf unseren zähler pos um den nächsten buchstaben zu erhalten
			if wort[pos+1] == 'a': 
				result = result + 'か'
				# hier True setzen, weil wir schon den zweiten buchstaben betrachten!
				skip = True
			# TODO: vervollständigen

		# TODO: s-reihe hinzufügen

		if   wort[pos] == 'a': result = result + 'あ'
		elif wort[pos] == 'i': result = result + 'い'
		elif wort[pos] == 'u': result = result + 'う'
		elif wort[pos] == 'e': result = result + 'え'
		elif wort[pos] == 'o': result = result + 'お'
		
		elif wort[pos] == 'n': result = result + 'ん'

	# nach dem for-loop soll das ergebnis ausgegeben werden
	print(result)

# test-wort
test = "akae"

# hier wird die funktion mit der eingabe des test-wortes aufgerufen
converter(test)

# "kaa"  -> "かあ""
# "akae" -> "あかえ"
