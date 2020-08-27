# Rekursion allgemein für Listen
# ein for-loop kann eine Liste mittels dem index durchlaufen, dafür schreibt man
# for index in (range(len(liste))) (len -> length)
# eine rekursion macht das auch, ohne dass man index bzw. länge wissen muss
# damit wir die rekursion noch besser nutzen können erweitern wir mit dem sogenannten pattern matching
# das ist im besonderen das denken von head und tail, also das die liste so [.][....] aussieht

# fangen wir mit der rekursion an. wie ich versprochen habe lösen wir die logik vom content ab.

# strings wie 'okarina' sind auch listen, zumindest werden sie auch behandelt.
# im for-loop haben wir mit += strings zusammengefügt, also sprich konkateniert.
# genau deswegen können wir auch strings mit einem index abfragen
# sei wort = "okarina"
# dann ist wort[0] = 'o', wort[1] = 'k', etc

# wieder erhält die convert-funktion ein wort - welchen typ 'wort' hat müssen wir erstmal nicht angebenen (danke python),
# deshalb gehen wir geschickter weise davon aus dass schon hiragana-pakete ankommen ['o', 'ka', 'ri', 'na']

def convert(wort):

	# jetzt definieren wir uns erstmal head und tail
	
	# head, tail = wort[0], wort[1:]
	
	# [1:] wtf?
	# das bedeutet "ab 1 bis ende"

	# jetzt überlegen wir uns die fälle.
	# was ist unsere abbruchbedingung? nun, wir können wählen zwischen:
	# das wort ist leer (einfach aufhören) oder das wort hat nurnoch eine länge (nurnoch eine aktion)
	# ersteres will ich nicht, da dass für mich ein unnötiger rekursionsschritt ist

	# if len(xs) == 1: return ???

	# daneben gibt es noch den normalen arbeitsschritt: eine liste bauen

	# else: return ??? + converter(tail)

	# das war's. die logik stellt nur 3 zeilen dar,
	# aber noch sind wir nicht fertig. ??? müssen noch definiert werden
	# überlegen wir uns, ob es eine möglichkeit gibt, direkt nach der "form" des heads zu fragen,
	# ist head == 'o'? aber um die vielen ifs zu vermeiden, kombinieren wir jetzt unser wissen über listen.
	# angenommen wir hätten eine liste, die einen 'schlüssel' braucht und dir den jeweiligen 'value' zurückgibt.
	# dann müssten wir nurnoch schreiben
	# tolleListe[head] und zack, wir haben das gewünschte ergebnis.
	# tatsache, so eine tolle liste exisiert und man nennt sie (hash)maps oder dictionaries:
	# hashmap = { schlüssel_1 : value_1, schlüssel_2 : value_2, etc } 
	# wenn man so eine hashmap hat, dann füttert man ihr schlüssel wie bei listen einen index

	head, tail = wort[0], wort[1:]
	if len(wort) == 1: return hiragana_map[head]
	else: return hiragana_map[head] + convert(tail)

# jetzt müssen wir uns auch die hashmap 'hiragana' kümmern.
# hiragana = {}
# aber die ist leer und statt sie mühselig aufzufüllen würde ich einen anderen weg gehen
# \u3040 \u309f (unicode)
# hier sind alle hiragana-zeichen drin (es gibt sogar noch leere slots)
# 3040 und 309f sind hexadezimal und sind dezimal betrachtet 12352 bis 12447

hiragana1 = [chr(x) for x in range(ord('\u3040'), ord('\u309f') + 1)]

# schöne liste, viel magic.
# mit [ (save this) for x in xs] erstelle ich ganz schnell eine liste für jedes element in der liste xs
# jedes x ist eine zahl, die erste ist 12532 und die letzte ist 12447
# daher schreiben wir chr(x), das nimmt eine zahl und gibt den unicode wert zurück, also genau unser gewünschtes hiragana
# dasselbe gilt auch für range, aber hier muss ich zusätzlich die unicode werde in ord verpacken (die umkehrfunktion von chr)

# aus dieser liste machen wir eine hashmap mit genau derselben magic:

hiragana2 = {hiragana1.index(x) : x for x in hiragana1}
#print(hiragana2)

# nun sind die hiragana an ihre index-werte gekoppelt. diese müssten von hand geändert und separat abgespeichert werden

# TODO: print(hiragana2) ausführen, die ausgegebene liste hier copy-pasten

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

# dann die einträge anpassen
# jeden ungültigen eintrag entfernen und jeden gültigen eintrag den richtigen schlüssel zu weisen, beispiel:
# 0: '\u3040'	-> löschen
# 1: 'ぁ'		-> löschen (ist ein sonderfall, beachten wir nicht)
# 2: 'あ'		-> 'a': 'あ'

# das macht man genau einmal und hat einen guten überblick auf die einträge.

######################## Teil 2 #################################

# unser plan: "okarina" -> ['o', 'ka', 'ri', 'na']
# wir sehen auch direkt ein muster, jede sible endet mit einem vokal
# also wollen wir eine liste mit allen vokalen

vokale = 'aeiou'

# wir machen das wieder rekursiv
# die aufgabe hier ist zwar anders als die vom converter, aber rekursion ist ein werkzeug und wir können es universal verwenden
# allerdings brauchen wir hier einen zwischenspeicher, denn wenn die rekursion erneut startet ist alles davor vergessen
# als wir die zahlen addiert oder die silben konvertiert haben war das ein eindimensionaler prozess (1 -> 1), aber 
# hier müssen wir uns daran erinnern, was wir zuvor gelesen haben. 

# > string_to_list('okarina', '')
# > head -> 'o', tail -> 'karina'
# > (head in vokale?) -> verpacke zwischenspeicher als liste 
# > zwischenspeicher = [zwischenspeicher + head]
# > zwischenspeicher + string_to_list(tail, '')
# > ansonten nur head in zwischenspeicher aufnehmen 
# > zwischenspeicher = zwischenspeicher + head
# > string_to_list(tail, zwischenspeicher)

# das ist unsere abbruchbedingung. wenn ein vokal gelesen wird, dann wird es noch in den zwischenspeicher aufgenommen,
# damit der zwischenspeicher eine vollständige silbe enthält. diese wird als liste verpackt und es geht von vorne los. 
# achtung !!! die zeilen 115 und 118 sehen verdächtig gleich aus.
# der unterschied ist der folgende: ist eine silbe vollständig, so soll sie als liste gespeichert werden, ansonten ist
# der zwischenspeicher nicht voll genug.

# > string_to_list('okarina', '')
# > ['o'] + string_to_list('karina', '')
# > ['o'] + string_to_list('arina', 'k')
# > ['o'] + ['ka'] + string_to_list('rina', '')
# > ['o'] + ['ka'] + string_to_list('ina', 'r')
# > ['o'] + ['ka'] + ['ri'] + string_to_list('na', '')
# > ['o'] + ['ka'] + ['ri'] + string_to_list('a', 'n')
# > ['o'] + ['ka'] + ['ri'] + ['na']
# > ['o', 'ka', 'ri', na]

# hier siehst du, dass sich der zwischenspeicher (= akkumulator, abgekürzt acc) mit konsonanten füllt.
# am schluss kommt unsere wunderschöne liste heraus

def string_to_list(w, acc):
	# die zeile ist echt immer gleich, richtig praktisch
	head, tail = w[0], w[1:] 

	# ist es unser letzter schritt? dann wissen wir, dass auch die silbe zuende sein muss
	# also nurnoch eben den head in den zwischenspeicher schreiben und das ding als liste zurückgeben
	if len(w) == 1:
		acc = [acc + head]
		return acc

	# lesen wir ein leerzeichen? wir setzen es auch in die neue liste ein
	# achtung! die hashmap braucht dafür den eintrag {' ' : ' '}, weil unser converter jedes element betrachtet
	# ODER wir bauen einen extra-fall für die rekursion des converters ein
	# ich bin für den eintrag, dafür haben wir doch eine hashmap
	elif head == ' ': 
		return [' '] + string_to_list(tail, '')

	# lesen wir gerade ein vokal? dann müsste die silbe zu ende sein
	# wir schreiben den head in den zwischenspeicher und geben das ding als liste zurück
	elif head in vokale:
		acc = [acc + head]
		return acc + string_to_list(tail, '')

	# spezialfall n
	# nach dem n muss ein konsonant (oder nichts) folgen
	elif (tail[0] not in vokale) & (head == 'n'): 
		return ['n'] + string_to_list(tail, '')
	
	# spezialfall kk, tt, ...
	# head und tail müssen die gleichen konsonanten sein
	elif (head not in vokale) & (tail[0] not in vokale) & (head == tail[0]): 
		return ['small tsu'] + string_to_list(tail, '')

	# die silbe ist wohl noch nicht zu ende
	# dann brauchen wir nurnoch den head in den zwischenspeicher zu schreiben und die rekursion fortsetzen
	else:
		acc = acc + head
		return string_to_list(tail, acc)

#print(string_to_list('okarina', ''))

# die 3 TODOs sind beinahe identisch!
# das wird entweder verdammt schnell gehen und gar nicht, das kann ich gerade nicht einschätzen, brauch dein feedback

# damit funktioniert der Hiragana Converter

# erster vers von SAO Intro 1 'Crossing Field' von LiSa
vers = 'Mitomete ita okubyou na kako Wakaranai mama ni kowagatte ita Ushiro no jibun ga genjitsu wo ima ni utsusu'.lower()
zerhackter_vers = string_to_list(vers, '')
print(convert(zerhackter_vers))



