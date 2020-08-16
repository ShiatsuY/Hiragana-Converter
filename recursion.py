def error(): raise ValueError('Something went wrong!')

# wir beginnen mit der funktion, die für eine zahl n alle zahlen von 1 bis n addieren soll
# bevor wir zur rekursion kommen möchte ich die version ohne rekursion zeigen
# der for-loop ist ein nützliches mittel, aber der while-loop ist gleichmächtig
# wir führen eine aktion immer wieder aus, bis eine bedingung erreicht wird (ähnlich wie das erreichen vom ende des for-loops)
# (beides basiert im prinzip auf ifs in ihrer logik)

def sumFor(n):
	if n < 1: error()
	result = 0
	for x in range(n): result += x + 1 # frage: wieso steht hier + 1?
	return result

def sumWhile(n):
	if n < 1: error()
	result = 0
	while n > 0:
		result += n
		n += -1 # frage: wieso steht hier - 1?
	return result

# beide varianten leiden unter dem gleichen problem: sie sind abhängig vom zwischenspeicher result.
# stell dir eine netzwerkverbindung vor, die instabil sein könnte. wenn es einen aussetzer in der verbindung gibt, dann könnte
# 1. der zwischenspeicher einen zwischenschritt verpassen
# 2. es wird ein error geworfen weil er den zwischenspeicher nicht mehr finden kann (result ging verloren)
# das ist nur ein aspekt, aber das ist schon ein gravierender nachteil
# von der performance ganz zu schweigen (jeder schritt ist eine operation)

# rekursion funktionert ganz anders in der hinsicht!
# das, was zu berechnen ist, wird erst "aufbereitet", sodass nurnoch ein einziger befehl am ende ausgeführt werden muss
# dadurch hat rekursion keines dieser nachteile, auch nicht in anderen aspekten

# ein anderer wichtiger punkt ist, dass wir hier keine festen hiragana-zeichen benutzen, sondern eine variable zahl
# der massive vorteil der rekursion ist, dass dieser feste teil eines programmes nicht in der logik zu finden ist, sondern ausgelagert wird
# eben genau so, wie wir es mit result gemacht haben, wäre dieser feste teil sogar eine globale variable
# (result ist nur sichtbar für die funktion die sie erschafft. deswegen können in den beiden sum-varianten auch gleichnamige result stehen. sie haben nichts miteinander zu tun!)
# wir wollen also logik von inhalten trennen. wäre doch genial, wenn man die nackte logik oder den reinen inhalt betrachten könnte

# recursion let's go!
# n soll eine natürliche zahl sein, deswegen müssen wir das checken
# wir müssen insgesamt 3 fälle beachten:
# ist n kleiner als 1? -> abbrechen
# ist n gleich 1? -> rekursion beenden
# ansonsten -> n + sum(n-1)

def sumRecursion(n):
	if n < 1: error()
	elif n == 1: return 1
	else: return n + sumRecursion(n-1)

# sei n = 5
# dann fallen wir immer wieder in den dritten fall, bis n = 1 ist:
# (das zeichen > soll programm-denken darstellen)
# > 5 + sum(5-1)
# > 5 + 4 + sum(4-1)
# > 5 + 4 + 3 + sum(3-1)
# > 5 + 4 + 3 + 2 + sum(2-1)
# > 5 + 4 + 3 + 2 + 1
# > 15

# neu ist hier bei auch das statement "return"
# das müssen wir jetzt benutzen, weil das typsystem von python zur laufzeit nicht wissen wird, was sum(n) überhaupt ist. der compiler wird einen error ausgeben.
# angenommen, sum(n) bekommt anstatt eine zahl ein wort. dann bekommen wir einen fehler, weil n < 1 zu fragen ja schon nicht mehr funktioniert.
# angenommen, wir lassen "return" weg. dann haben wir das problem beim dritten fall: n + sum(n-1):
# sum(n) ist ja keine zahl, sondern eine funktion! also woher soll python wissen, dass sum(n) eigentlich auch nur zahlen als ausgabetyp hat?
# ganz einfach! indem wir mit "return" den ausgabetyp fixieren kann python das wissen und wird die funktion sum(n) als zahl zusätzlich interpretieren.

print(sumFor(5))
print(sumWhile(5))
print(sumRecursion(5))

#################
# aufgabenteil: #
#################

# fibonacci-zahlen werden wie folgt definiert:
# f(0) = 0
# f(1) = 1
# f(n) = f(n-1) + f(n-2)
# die ersten 10 zahlen sind:
# 0 1 1 2 3 5 8 13 21 34 88
# > f(3) = f(2) + f(1)
# > f(3) = (f(1) + f(0)) + f(1)
# > f(3) = (1 + 0) + 1
# > f(3) = 2
# die ersten 3 zahlen sind: 0 1 1 und ihre summe ist 2

# deine aufgabe ist es eine rekursive version zu schreiben

# for-loop
def fibLoop(n):
	if n < 0: error()
	result, n1, n2 = 0, 0, 1

	for x in range(0, n):
		result += n1 
		temp = n1 + n2
		n1 = n2
		n2 = temp

	return result

# while-loop
def fibWhile(n):
	if n < 0: error()
	result, n1, n2, counter = 0, 0, 1, 1

	while (counter <= n):
		result += n1
		temp = n1 + n2
		n1 = n2
		n2 = temp

		counter += 1

	return result

# rekursion
def fibRecursion(n): 
	# TODO
	error()

print(fibLoop(5))
print(fibWhile(5))
#print(fibRecursion(5))
