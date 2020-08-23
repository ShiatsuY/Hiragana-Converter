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
	if len(xs) == 1: return hiragana[head]
	else: return hiragana[head] + converter(tail)

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
print(hiragana2)

# nun sind die hiragana an ihre index-werte gekoppelt. diese müssten von hand geändert und separat abgespeichert werden

# TODO: print(hiragana2) ausführen, die ausgegebene liste hier copy-pasten

# hiraganaMap = { ... }

# dann die einträge anpassen
# jeden ungültigen eintrag entfernen und jeden gültigen eintrag den richtigen schlüssel zu weisen, beispiel:
# 0: '\u3040'	-> löschen
# 1: 'ぁ'		-> löschen (ist ein sonderfall, beachten wir nicht)
# 2: 'あ'		-> 'a': 'あ'

# das macht man genau einmal und hat einen guten überblick auf die einträge.


# nächstes mal: mache aus 'watashi' -> ['wa', 'ta', 'shi']
