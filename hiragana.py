# for-schleife
# jeder buchstabe des wortes wird einzeln betrachtet
# result ist der speicher, hier werden die konvertierten zeichen gespeichert
def converter(wort):
	# speicher
	result = ''

	# das hier ist eine sogenannte Flagge
	# sie wird genau dann True gesetzt, wenn wir eine Iteration überspringen wollen
	# sie wird anfangs auf False gesetzt, damit sie nicht gleich etwas bewirkt
	# sie sorgt dafür, dass man einen Buchstabeen skippt
	skip = False

	# um einen weiteren Buchstaben zu skippen braucht man ne zweite Flagge
	skip2 = False



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

		if skip2:
			skip2 = False
			continue

		
		# k-reihe
		if wort[pos] == 'k':

			# um den nächsten buchstaben schon zu betrachten benutzen wir einen kleinen trick:
			# wir addieren eine 1 auf unseren zähler pos um den nächsten buchstaben zu erhalten
			if wort[pos+1] == 'a': 
				result = result + 'か'
				# hier True setzen, weil wir schon den zweiten buchstaben betrachten!
				skip = True
			if wort[pos+1] == 'i':
				result = result + 'き'
				skip = True
			if wort[pos+1] == 'u':
				result = result + 'く'
				skip = True
			if wort[pos+1] == 'e':
				result = result + 'け'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'こ'
				skip = True

		# s-Reihe
		if wort[pos] == 's':

			if wort[pos+1] == 'a':
				result = result + 'さ'
				skip = True

			if wort[pos+1] == 'h':
				
				skip = True



				
				

				#Da man mit shi drei Buchstaben hat muss man es genauer definieren

				if wort[pos+2] == 'i':
					result = result + 'し'
					skip2 = True

			if wort[pos+1] == 'u':
				result = result + 'す'
				skip = True
			if wort[pos+1] == 'e':
				result = result + 'せ'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'そ'
				skip = True

		# t-Reihe  ta chi! tsu! te to
		if wort[pos] == 't':

			# um den nächsten buchstaben schon zu betrachten benutzen wir einen kleinen trick:
			# wir addieren eine 1 auf unseren zähler pos um den nächsten buchstaben zu erhalten
			if wort[pos+1] == 'a': 
				result = result + 'た'
				# hier True setzen, weil wir schon den zweiten buchstaben betrachten!
				skip = True
			
			# if wort[pos+1] == 'c':
				result = result + 'ち'
				skip = True
				
			if wort[pos+1] == 's':
				skip = True
				if wort[pos+2] == 'u':
					result = result + 'つ'
					skip2 = True

			if wort[pos+1] == 'e':
				result = result + 'て'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'と'
				skip = True		


		if wort[pos] == 'n':

			if wort[pos+1] == 'a': 
				result = result + 'な'
				skip = True
			if wort[pos+1] == 'i':
				result = result + 'に'
				skip = True
			if wort[pos+1] == 'u':
				result = result + 'ぬ'
				skip = True
			if wort[pos+1] == 'e':
				result = result + 'ね'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'の'
				skip = True


		if wort[pos] == 'h':

			# ha hi fu! he ho

			if wort[pos+1] == 'a': 
				result = result + 'は'
				skip = True
			if wort[pos+1] == 'i':
				result = result + 'ひ'
				skip = True
			#if wort[pos+1] == 'u':
				result = result + 'ふ'
				skip = True
			if wort[pos+1] == 'e':
				result = result + 'へ'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'ほ'
				skip = True


		if wort[pos] == 'm':

			if wort[pos+1] == 'a': 
				result = result + 'ま'
				skip = True
			if wort[pos+1] == 'i':
				result = result + 'み'
				skip = True
			if wort[pos+1] == 'u':
				result = result + 'む'
				skip = True
			if wort[pos+1] == 'e':
				result = result + 'め'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'も'
				skip = True


		if wort[pos] == 'y':

			if wort[pos+1] == 'a': 
				result = result + 'や'
				skip = True
			if wort[pos+1] == 'u':
				result = result + 'ゆ'
				skip = True		
			if wort[pos+1] == 'o':
				result = result + 'よ'
				skip = True


		if wort[pos] == 'r':

			if wort[pos+1] == 'a': 
				result = result + 'ら'
				skip = True
			if wort[pos+1] == 'i':
				result = result + 'り'
				skip = True
			if wort[pos+1] == 'u':
				result = result + 'る'
				skip = True
			if wort[pos+1] == 'e':
				result = result + 'れ'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'ろ'
				skip = True


		if wort[pos] == 'w':
			if wort[pos+1] == 'a':
				result = result + 'わ'
				skip = True

			if wort[pos+1] == 'o':
				result = result + 'を'
				skip = True


		if wort[pos] == 'g':

			if wort[pos+1] == 'a': 
				result = result + 'が'
				skip = True
			if wort[pos+1] == 'i':
				result = result + 'ぎ'
				skip = True
			if wort[pos+1] == 'u':
				result = result + 'ぐ'
				skip = True
			if wort[pos+1] == 'e':
				result = result + 'げ'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'ご'
				skip = True


		if wort[pos] == 'b':

			if wort[pos+1] == 'a': 
				result = result + 'ば'
				skip = True
			if wort[pos+1] == 'i':
				result = result + 'び'
				skip = True
			if wort[pos+1] == 'u':
				result = result + 'ぶ'
				skip = True
			if wort[pos+1] == 'e':
				result = result + 'べ'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'ぼ'
				skip = True


		if wort[pos] == 'p':

			if wort[pos+1] == 'a': 
				result = result + 'ぱ'
				skip = True
			if wort[pos+1] == 'i':
				result = result + 'ぴ'
				skip = True
			if wort[pos+1] == 'u':
				result = result + 'ぷ'
				skip = True
			if wort[pos+1] == 'e':
				result = result + 'ぺ'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'ぽ'
				skip = True


		if wort[pos] == 'd':

			if wort[pos+1] == 'a': 
				result = result + 'だ'
				skip = True
			#if wort[pos+1] == 'i':
				result = result + 'ぴ'
				skip = True
			#if wort[pos+1] == 'u':
				result = result + 'ぷ'
				skip = True
			if wort[pos+1] == 'e':
				result = result + 'で'
				skip = True
			if wort[pos+1] == 'o':
				result = result + 'ど'
				skip = True




		

		if   wort[pos] == 'a': result = result + 'あ'
		elif wort[pos] == 'i': result = result + 'い'
		elif wort[pos] == 'u': result = result + 'う'
		elif wort[pos] == 'e': result = result + 'え'
		elif wort[pos] == 'o': result = result + 'お'
		
		elif wort[pos] == 'n': result = result + 'ん'

	# nach dem for-loop soll das ergebnis ausgegeben werden
	print(result)

# test-wort
#test = "kakikukeko"
test = "dadehipo"
# hier wird die funktion mit der eingabe des test-wortes aufgerufen
converter(test)

# "kaa"  -> "かあ""
# "akae" -> "あかえ"
