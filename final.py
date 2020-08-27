vokale = 'aeiou'
xs = 'ゃゅょ'
hiragana_map = {' ' : ' ', 'a': 'あ', 'i': 'い','u': 'う','e': 'え','o': 'お', 'ka': 'か', 'ga': 'が','ki': 'き', 'gi': 'ぎ', 'ku': 'く', 'gu': 'ぐ', 'ke': 'け', 'ge': 'げ',
'ko': 'こ','go': 'ご', 'sa': 'さ', 'za': 'ざ', 'shi': 'し', 'ji': 'じ', 'su': 'す', 'zu': 'ず', 'se': 'せ', 'ze': 'ぜ', 'so': 'そ', 'zo': 'ぞ',
'ta': 'た','da': 'だ', 'chi': 'ち', 'di': 'ぢ', 'tsu':'つ', 'du': 'づ', 'te': 'て', 'de': 'で', 'to': 'と', 'do': 'ど', 'na': 'な', 'ni': 'に', 'nu': 'ぬ',
'ne': 'ね', 'no': 'の', 'ha': 'は', 'ba': 'ば', 'pa': 'ぱ', 'hi': 'ひ', 'bi': 'び', 'pi': 'ぴ', 'fu': 'ふ', 'bu': 'ぶ', 'pu': 'ぷ', 'he': 'へ',
'be': 'べ', 'pe': 'ぺ', 'ho': 'ほ', 'bo': 'ぼ', 'po': 'ぽ', 'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も', 'ya':'や','yu': 'ゆ',
'yo':'よ', 'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ','wa': 'わ', 'wo': 'を', 'n': 'ん', 'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
'sha': 'しゃ', 'shu':'しゅ','sho': 'しょ', 'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ', 'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ', 'hya': 'ひゃ',
'hyu': 'ひゅ', 'hyo': 'ひょ', 'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ', 'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ', 'gya': 'ぎゃ', 'gyu': 'ぎゅ',
'gyo': 'ぎょ', 'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ', 'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ', 'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
'small tsu' : 'っ'}

string_map = {value : key for key, value in hiragana_map.items()}

def convert_to_hiragana(wort):
	head, tail = wort[0], wort[1:]
	if len(wort) == 1: return hiragana_map[head]
	else: return hiragana_map[head] + convert_to_hiragana(tail)

def convert_to_string(wort):
	head, tail = wort[0], wort[1:]
	if len(wort) == 1: return string_map[head]
	else: return string_map[head] + convert_to_string(tail)

def string_to_list(wort, acc):
	head, tail = wort[0], wort[1:] 
	if len(wort) == 1: return [acc + head]
	elif head == ' ': return [' '] + string_to_list(tail, '')
	elif head in vokale: return [acc + head] + string_to_list(tail, '')
	elif (tail[0] not in vokale) & (head == 'n'): return ['n'] + string_to_list(tail, '')
	elif (head not in vokale) & (tail[0] not in vokale) & (head == tail[0]): return ['small tsu'] + string_to_list(tail, '')
	else: return string_to_list(tail, acc + head)

def hiragana_to_list(wort, acc):
	head, tail = wort[0], wort[1:]
	if len(wort) == 1: return [acc + head]
	if (len(wort) == 2) & (tail[0] in xs): return [head + tail[0]]
	elif head == ' ': return [' '] + hiragana_to_list(tail, '')
	elif  tail[0] in xs: return [head + tail[0]] + hiragana_to_list(tail[1:], '')
	else: return [head] + hiragana_to_list(tail, acc) 

def is_romaji(wort):
	try: return wort[0].encode('ascii').isalpha() 
	except: return False

def test():
	vers = 'Mitomete ita okubyou na kako Wakaranai mama ni kowagatte ita Ushiro no jibun ga genjitsu wo ima ni utsusu '.lower()
	zerhackter_vers = string_to_list(vers, '')
	ergebnis = convert_to_hiragana(zerhackter_vers)
	print('Romaji Input:    ' + vers)
	print('Hiragana Output: ' + ergebnis)

	print('-----------------------')

	vers2 = ergebnis
	zerhackter_vers2 = hiragana_to_list(vers2, '')
	ergebnis2 = convert_to_string(zerhackter_vers2)
	print('Hiragana Input:  ' + vers2)
	print('Romaji Output:   ' + ergebnis2)

def main():
	user_input = input('Write something in Hiragana or Romaji: ')
	print('You wrote: ' + user_input)
	if is_romaji(user_input): print(convert_to_hiragana(string_to_list(user_input.lower(), '')))
	else: print(convert_to_string(hiragana_to_list(user_input, ''))) 

main()
