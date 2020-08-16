def error(): raise ValueError('Something went wrong!')

def converter(wort):
	result = ''
	skip = False
	skip2 = False
	positions = range(len(wort))
	length = len(wort)
	
	for pos in positions:

		if skip:
			skip = False 
			continue
		if skip2:
			skip2 = False
			continue

		# k-reihe
		if wort[pos] == 'k':
			if wort[pos+1] == 'a': result += 'か'
			elif wort[pos+1] == 'i': result += 'き'
			elif wort[pos+1] == 'u': result += 'く'
			elif wort[pos+1] == 'e': result += 'け'
			elif wort[pos+1] == 'o': result += 'こ'
			# kya kyu kyo	
			elif wort[pos+1] == 'y':
				if wort[pos+2] == 'a': result += 'きゃ'
				elif wort[pos+2] == 'u': result += 'きゅ'
				elif wort[pos+2] == 'o': result += 'きょ'
				else: error()
				skip2 = True
			else: error()
			skip = True
			
		# s-Reihe
		elif wort[pos] == 's':
			if wort[pos+1] == 'a': result += 'さ'
			elif wort[pos+1] == 'h':
				if wort[pos+2] == 'i': result += 'し'
				else: error()
				skip2 = True
			elif wort[pos+1] == 'u': result += 'す'
			elif wort[pos+1] == 'e': result += 'せ'
			elif wort[pos+1] == 'o': result += 'そ'
			# sha shu sho	
			elif wort[pos+1] == 'h':
				if wort[pos+2] == 'a': result += 'しゃ'
				elif wort[pos+2] == 'u': result += 'しゅ'
				elif wort[pos+2] == 'o': result += 'しょ'
				else: error()
				skip2 = True
			else: error()
			skip = True
			
		# t-reihe
		elif wort[pos] == 't':
			if wort[pos+1] == 'a': result += 'た'	
			elif wort[pos+1] == 's':
				if wort[pos+2] == 'u': result += 'つ'
				else: error()
				skip2 = True
			elif wort[pos+1] == 'e': result += 'て'
			elif wort[pos+1] == 'o': result += 'と'
			else: error()	
			skip = True	
			
		# cha chi chu cho 
		elif wort[pos] == 'c':
			if wort[pos+1] == 'h':
				if wort[pos+2] == 'a': result += 'ちゃ'
				elif wort[pos+2] == 'i': result += 'ち'
				elif wort[pos+2] == 'u': result += 'ちゅ'
				elif wort[pos+2] == 'o': result += 'ちょ'
				else: error()
				skip2 = True
			else: error()
			skip = True
			
		# n-reihe
		elif wort[pos] == 'n': 
			if pos == length-1: result += 'ん'
			elif wort[pos+1] == 'a': result += 'な'
			elif wort[pos+1] == 'i': result += 'に'
			elif wort[pos+1] == 'u': result += 'ぬ'
			elif wort[pos+1] == 'e': result += 'ね'
			elif wort[pos+1] == 'o': result += 'の'
			# nya nyu nyo	
			elif wort[pos+1] == 'y':
				if wort[pos+2] == 'a': result += 'にゃ'
				elif wort[pos+2] == 'u': result += 'にゅ'
				elif wort[pos+2] == 'o': result += 'にょ'
				else: error()
				skip2 = True

			else: result += 'ん'
			skip = True
			
		# h-Reihe
		elif wort[pos] == 'h':
			# ha hi fu! he ho
			if wort[pos+1] == 'a': result += 'は'				
			elif wort[pos+1] == 'i': result += 'ひ'					
			elif wort[pos+1] == 'e': result += 'へ'				
			elif wort[pos+1] == 'o': result += 'ほ'				
			# hya hyu hyo	
			elif wort[pos+1] == 'y':
				if wort[pos+2] == 'a': result += 'ひゃ'
				elif wort[pos+2] == 'u': result += 'ひゅ'
				elif wort[pos+2] == 'o': result += 'ひょ'
				else: error()
				skip2 = True
			else: error()
			skip = True
			
		# fu
		elif wort[pos] == 'f':
			if wort[pos+1] == 'u': result += 'ふ'
			else: error()
			skip = True 
			
		# m-reihe
		elif wort[pos] == 'm':
			if wort[pos+1] == 'a': result += 'ま'				
			elif wort[pos+1] == 'i': result += 'み'
			elif wort[pos+1] == 'u': result += 'む'				
			elif wort[pos+1] == 'e': result += 'め'				
			elif wort[pos+1] == 'o': result += 'も'
			# mya myu myo	
			elif wort[pos+1] == 'y':
				if wort[pos+2] == 'a': result += 'みゃ'
				elif wort[pos+2] == 'u': result += 'みゅ'
				elif wort[pos+2] == 'o': result += 'みょ'
				else: error()
				skip2 = True
			else: error()
			skip = True
			
		# y-reihe
		elif wort[pos] == 'y':
			if wort[pos+1] == 'a': result += 'や'		
			elif wort[pos+1] == 'u': result += 'ゆ'	
			elif wort[pos+1] == 'o': result += 'よ'
			else: error()
			skip = True
			
		# r-reihe
		elif wort[pos] == 'r':
			if wort[pos+1] == 'a': result += 'ら'				
			elif wort[pos+1] == 'i': result += 'り'		
			elif wort[pos+1] == 'u': result += 'る'			
			elif wort[pos+1] == 'e': result += 'れ'			
			elif wort[pos+1] == 'o': result += 'ろ'			
			# rya ryu ryo	
			elif wort[pos+1] == 'y':
				if wort[pos+2] == 'a': result += 'りゃ'
				elif wort[pos+2] == 'u': result += 'りゅ'
				elif wort[pos+2] == 'o': result += 'りょ'
				else: error()
				skip2 = True		
			else: error()
			skip = True
			
		# w-reihe
		elif wort[pos] == 'w':
			if wort[pos+1] == 'a': result += 'わ'				
			elif wort[pos+1] == 'o': result += 'を'
			else: error()
			skip = True
			
		# g-reihe
		elif wort[pos] == 'g':
			if wort[pos+1] == 'a': result += 'が'				
			elif wort[pos+1] == 'i': result += 'ぎ'				
			elif wort[pos+1] == 'u': result += 'ぐ'				
			elif wort[pos+1] == 'e': result += 'げ'				
			elif wort[pos+1] == 'o': result += 'ご'
			# gya gyu gyo	
			elif wort[pos+1] == 'y':
				if wort[pos+2] == 'a': result += 'ぎゃ'
				elif wort[pos+2] == 'u': result += 'ぎゅ'
				elif wort[pos+2] == 'o': result += 'ぎょ'
				else: error()
				skip2 = True
			else: error()
			skip = True
			
		# z-reihe
		elif wort[pos] == 'z':
			if wort[pos+1] == 'a': result += 'ざ'						
			elif wort[pos+1] == 'u': result += 'ず'				
			elif wort[pos+1] == 'e': result += 'ぜ'				
			elif wort[pos+1] == 'o': result += 'ぞ'
			else: error()
			skip = True	
			
		# j-Reihe
		elif wort[pos] == 'j':
			if wort[pos+1] == 'a': result += 'じゃ'
			elif wort[pos+1] == 'i': result += 'じ'
			elif wort[pos+1] == 'u': result += 'じゅ'
			elif wort[pos+1] == 'o': result += 'じょ'
			else: error()
			skip = True
			
		# b-Reihe
		elif wort[pos] == 'b':
			if wort[pos+1] == 'a': result += 'ば'			
			elif wort[pos+1] == 'i': result += 'び'				
			elif wort[pos+1] == 'u': result += 'ぶ'				
			elif wort[pos+1] == 'e': result += 'べ'				
			elif wort[pos+1] == 'o': result += 'ぼ'
			# bya byu byo	
			elif wort[pos+1] == 'y':
				if wort[pos+2] == 'a': result += 'びゃ'
				elif wort[pos+2] == 'u': result += 'びゅ'
				elif wort[pos+2] == 'o': result += 'びょ'
				else: error()
				skip2 = True
			else: error()
			skip = True
			
		# p-Reihe
		elif wort[pos] == 'p':
			if wort[pos+1] == 'a': result += 'ぱ'				
			elif wort[pos+1] == 'i': result += 'ぴ'				
			elif wort[pos+1] == 'u': result += 'ぷ'				
			elif wort[pos+1] == 'e': result += 'ぺ'				
			elif wort[pos+1] == 'o': result += 'ぽ'
			# pya pyu pyo	
			elif wort[pos+1] == 'y':
				if wort[pos+2] == 'a': result += 'ぴゃ'
				elif wort[pos+2] == 'u': result += 'ぴゅ'
				elif wort[pos+2] == 'o': result += 'ぴょ'
				else: error()
				skip2 = True
			else: error()
			skip = True
			
		# d-Reihe
		elif wort[pos] == 'd':
			if wort[pos+1] == 'a': result += 'だ'
			elif wort[pos+1] == 'i': result += 'ぢ'				
			elif wort[pos+1] == 'u': result += 'づ'				
			elif wort[pos+1] == 'e': result += 'で'				
			elif wort[pos+1] == 'o': result += 'ど'
			else: error()
			skip = True
			
		# vokale
		elif wort[pos] == 'a': result += 'あ'
		elif wort[pos] == 'i': result += 'い'
		elif wort[pos] == 'u': result += 'う'
		elif wort[pos] == 'e': result += 'え'
		elif wort[pos] == 'o': result += 'お'
			
		else: error()
	print(result)
