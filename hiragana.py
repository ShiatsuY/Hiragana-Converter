def error(): raise ValueError('Something went wrong!')

def converter(wort):
	result = ''
	skip = False
	skip2 = False
	
	for pos in range(len(wort)):

		if skip:
			skip = False 
			continue
		if skip2:
			skip2 = False
			continue

		# k-reihe
		if wort[pos] == 'k':
			if wort[pos+1] == 'a': 
				result += 'か'
			elif wort[pos+1] == 'i':
				result += 'き'
			elif wort[pos+1] == 'u':
				result += 'く'
			elif wort[pos+1] == 'e':
				result += 'け'
			elif wort[pos+1] == 'o': 
				result += 'こ'
			else: error()
			skip = True

		# s-Reihe
		elif wort[pos] == 's':
			if wort[pos+1] == 'a':
				result += 'さ'
			elif wort[pos+1] == 'h':
				if wort[pos+2] == 'i':
					result = result + 'し'
				else: error()
				skip2 = True
			elif wort[pos+1] == 'u':
				result = result + 'す'
			elif wort[pos+1] == 'e':
				result = result + 'せ'
			elif wort[pos+1] == 'o':
				result += 'そ'
			else: error()
			skip = True

		# t-reihe
		elif wort[pos] == 't':
			if wort[pos+1] == 'a': 
				result += 'た'	
			elif wort[pos+1] == 's':
				if wort[pos+2] == 'u':
					result += 'つ'
				else: error()
				skip2 = True
			elif wort[pos+1] == 'e':
				result += 'て'
			elif wort[pos+1] == 'o':
				result += 'と'
			else: error()	
			skip = True		

		# chi 
		elif wort[pos] == 'c':
			if wort[pos+1] == 'h':
				if wort[pos+2] == 'i':
					result += 'ち'
				else: error()
				skip2 = True
			else: error()
			skip = True

		# n-reihe
		elif wort[pos] == 'n':
			if wort[pos+1] == 'a': 
				result += 'な'
			elif wort[pos+1] == 'i':
				result += 'に'
			elif wort[pos+1] == 'u':
				result += 'ぬ'
			elif wort[pos+1] == 'e':
				result += 'ね'
			elif wort[pos+1] == 'o':
				result += 'の'
			else: result += 'ん'
			skip = True



####################################
#	ab hier weitermachen       #
####################################

		elif wort[pos] == 'h':

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


		elif wort[pos] == 'm':

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


		elif wort[pos] == 'y':

			if wort[pos+1] == 'a': 
				result = result + 'や'
				skip = True
			if wort[pos+1] == 'u':
				result = result + 'ゆ'
				skip = True		
			if wort[pos+1] == 'o':
				result = result + 'よ'
				skip = True


		elif wort[pos] == 'r':

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


		elif wort[pos] == 'w':
			if wort[pos+1] == 'a':
				result = result + 'わ'
				skip = True

			if wort[pos+1] == 'o':
				result = result + 'を'
				skip = True


		elif wort[pos] == 'g':

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


		elif wort[pos] == 'b':

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


		elif wort[pos] == 'p':

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


		elif wort[pos] == 'd':

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

		elif wort[pos] == 'a': result = result + 'あ'
		elif wort[pos] == 'i': result = result + 'い'
		elif wort[pos] == 'u': result = result + 'う'
		elif wort[pos] == 'e': result = result + 'え'
		elif wort[pos] == 'o': result = result + 'お'

		else: raise ValueError('Something went wrong!')

	print(result)

ktest = "kakikukeko"
stest = "sashisuseso"
ttest = "tachitsuteto"
converter(stest)
