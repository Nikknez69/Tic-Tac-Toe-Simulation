#Nikola Knezevic, Lya Marti & Simon Heller
#22.04.2024
#Program zum Simulieren von Gewinnwahrscheinlichkeiten in Tic Tac Toe

'''
Wir werden die Wahrscheinlichkeit des Gewinnens für einen Spieler für verschiedene Szenarien schätzen.
Spiel1: Eine Anzahl von Spielen wird zwischen zwei unerfahrenen (durch Zufall) Spielern gespielt. Es wird die Gewinnswahrscheinlichkeit für Spieler1 berechnet. Spieler1 beginnt.
Es gibt zwei Spieler: Spieler1 und Spieler2
'''
#Imports:
import random

# Das Programm wird "verschönert"
# Die Anzahl Versuche (n) wird definiert und abgefragt

print("*********************************************")
n = int(input("Anzahl Versuche: "))
print("*********************************************")

# Es gibt 9 Felder nummeriert von Feld0 bis Feld9
# Ein Wert von 0 für ein Feld bedeutet, dass das Feld nicht markiert wurde
# Ein Wert von 1 zeigt an, dass das Feld von Spieler-1 markiert wurde
# Ein Wert von 2 zeigt an, dass das Feld von Spieler-2 markiert wurde

feld1 = 0
feld2 = 0
feld3 = 0
feld4 = 0
feld5 = 0
feld6 = 0
feld7 = 0
feld8 = 0
feld9 = 0
spieler1 = 1
spieler2 = 2

#Die Variable 'zug' definiert, wessen Zug es gerade ist
zug = 1

def gueltiger_zug(zug):
	"""Bestimmt ob ein Zug gültig ist"""
	#Dieser Befehlt schaut, ob ein Zug ein erlaubter/gültiger Zug ist. Falls dieser Befehlt den Boolschen Wert "True" zurückgibt, kann der Zug gemacht werden. Falls "False" zurückkommt, wird ein anderer zufälliger Zug gespielt.
	if ((zug == 1 and feld1 == 0) or
		(zug == 2 and feld2 == 0) or
		(zug == 3 and feld3 == 0) or
		(zug == 4 and feld4 == 0) or
		(zug == 5 and feld5 == 0) or
		(zug == 6 and feld6 == 0) or
		(zug == 7 and feld7 == 0) or
		(zug == 8 and feld8 == 0) or
		(zug == 9 and feld9 == 0)):
		return True
	else:
		return False		

def sieg():
	"""Bestimmt, wann ein Spieler gewinnt"""
#Hier ist s1 ein Sieg für Spieler1, da es den Sieg durch eine Multiplikation von den Werten von 3 aneinanderliegenden Feldern definiert.
#s2 macht dasselbe, jedoch für Spieler2. Der Unterschied ist die Condition "___ == 8".
#Diese ist da, weil die Felder von Spieler2 mit einer "2" markiert werden und somit 2*2*2 (=2^3) = 8 gelten muss, um s2 zu erfüllen.
	s1 = (feld1 * feld2 * feld3 == 1 or
		  feld4 * feld5 * feld6 == 1 or
		  feld7 * feld8 * feld9 == 1 or
		  feld1 * feld4 * feld7 == 1 or
		  feld2 * feld5 * feld8 == 1 or
		  feld3 * feld6 * feld9 == 1 or
		  feld1 * feld5 * feld9 == 1 or
		  feld3 * feld5 * feld7 == 1) 
	s2 = (feld1 * feld2 * feld3 == 8 or
		  feld4 * feld5 * feld6 == 8 or
		  feld7 * feld8 * feld9 == 8 or
		  feld1 * feld4 * feld7 == 8 or
		  feld2 * feld5 * feld8 == 8 or
		  feld3 * feld6 * feld9 == 8 or
		  feld1 * feld5 * feld9 == 8 or
		  feld3 * feld5 * feld7 == 8) 
	if (s1 or s2):
		return True
	else:
		return False

def unerfahrener_zug():
	"""Definiert einen Zug, welcher eine Markierung völlig zufällig auf ein freies Feld setzt"""
	#Dieser "unerfahrene" Zug sollte eine Person simulieren, welche zufällige Markierung auf ein freies Feld im Tic-Tac-Toe-Spiel setzen
	y = random.randint(1, 9)
	if (gueltiger_zug(y) == True):
		return y
	else:
		return unerfahrener_zug()

def gueltiges_brett():
	"""Definiert, was ein gültiges Spiel/Spielbrett ist"""
	#Dieser Befehl definiert wie genau das Spielfeld aussieht. Dies ist vorallem wichtig, falls der Code nicht eindeutig verstanden werden kann von Menschen oder auch das Programm die Anreihung der Felder nicht versteht.
	p1 = 0
	p2 = 0
	for x in range(1, 10):
		if (eval('feld' + str(x)) == 1):
			p1 += 1
		elif (eval('feld' + str(x)) == 2):
			p2 += 1
	if (p1 >= p2):
		return True
	else:
		return False

def feld_markieren(nummer, spieler):
	"""Markiert die einzelnen Felder für einen Spieler"""
	#Dieser Befehl sorgt dafür, dass Felder von Spielern markiert werden können. Dies tut er indem er den Startwert der Felder (0) mit den jeweiligen Werten des ersten Spielers (1) oder des zweiten Spielers (2) ersetzt.
	#Da diese Markierungen Zahlen sind, kann beim Befehl "sieg()" mithilfe der Multiplikation geprüft werden, ob ein Spieler gewonnen hat.
	global feld1, feld2, feld3, feld4, feld5, feld6, feld7, feld8, feld9  
	global spieler1, spieler2, zug
	if (nummer == 1):
		feld1 = spieler
	elif (nummer == 2):
		feld2 = spieler
	elif (nummer == 3):
		feld3 = spieler
	elif (nummer == 4):
		feld4 = spieler
	elif (nummer == 5):
		feld5 = spieler
	elif (nummer == 6):
		feld6 = spieler
	elif (nummer == 7):
		feld7 = spieler
	elif (nummer == 8):
		feld8 = spieler
	elif (nummer == 9):
		feld9 = spieler

def felder_aktualisieren():
	"""Setzt die Felder wieder züruck (auf 0)"""
	#Damit man mehrere Male ein Tic-Tac-Toe-Spiel simulieren kann, muss man die Felder wieder auf ihren Startwert (0) setzen.
	#Damit man die Variabeln, welche ausserhalb des Befehls definiert sind verändern kann, nutzt man "global".
	global feld1, feld2, feld3, feld4, feld5, feld6, feld7, feld8, feld9  
	global spieler1, spieler2, zug
	feld1 = feld2 = feld3 = feld4 = feld5 = feld6 = feld7 = feld8 = feld9 = 0

def wer_ist_dran():
	"""Bestimmt wessen Zug ist jetzt"""
	#Damit man versichern kann, die Spieler nacheinander ihre Markierungen setzen, muss man jedem Spieler "sagen" wann er spielen darf. Genau dies tut dieser Befehl.
	#Dieser Befehl ist durchaus simpel. Falls der aktuelle Zug von Spieler1 gespielt wurde, wird die Variable "zug" auf "spieler2" gesetzt. Genau andersherum auch. Somit sorgt man dafür, dass die Spieler abwechselnd ihre Markierungen setzen.
	global feld1, feld2, feld3, feld4, feld5, feld6, feld7, feld8, feld9  
	global spieler1, spieler2, zug
	if (zug == spieler1):
		zug = spieler2
	else:
		zug = spieler1

def pruefen():
	"""Gibt true zurück, wenn eines der Felder 0 ist"""
	#Dieser Befehl prüft ob ein Feld noch den Startwert (0) hat.
	#Dies ist von Nutzen, um zu sehen, welche Felder noch frei sind.
	global feld1, feld2, feld3, feld4, feld5, feld6, feld7, feld8, feld9  
	global spieler1, spieler2, zug
	if ((feld1 * feld2 * feld3 * feld4 * feld5 * feld6 * feld7 * feld8 * feld9) == 0):
		return True
	else:
		return False

def spiel1(n):
	""" Gibt die totale Anzahl an Siegen für Spieler1 und die totale Anzahl an Unentschieden zurück. 
	
	n Spiele werden zwischen zwei unerfahrenen Spielern gespielt. Spieler1 beginnt.
	"""
	#Dieser Befehl ist das Herzstück der Simulation. Er kombiniert alle bisherigen Befehle und gibt zwei Werte zurück.
	#Diese Werte sind folgende: "anzahl_gewinne_sp1"(totale Anzahl an Siegen des Spieler1) & "unentschieden" (totale Anzahl an Unentschieden). Die Siege des zweiten Spielers werden nicht berücksichtigt, da man diese Zahl durch eine einfache Berechnung berechnen kann. Dies wird später auch getan.
	anzahl_gewinne_sp1 = 0
	unentschieden = 0
	for x in range(n):
		felder_aktualisieren()
		if (spiel(1) == 1):
			anzahl_gewinne_sp1 += 1
		elif (spiel(1) == 0):
			unentschieden += 1
	return anzahl_gewinne_sp1, unentschieden

def spiel(spieltyp=1):
	"""
	Gibt 1 zurück, wenn Spieler1 gewinnt und 2, wenn Spieler2 gewinnt, und 0, wenn es ein Unentschieden ist.
	"""
	#Dieser Befehl spielt ein einzelnes Tic-Tac-Toe-Spiel und gibt eine Zahl zwischen 0-2 basierend auf dem Ergebnis des Spiels zurück.
	#Diese Zahl (der Output) wird im spiel1()-Befehl gezählt und später ausgegeben.
	global feld1, feld2, feld3, feld4, feld5, feld6, feld7, feld8, feld9  
	global spieler1, spieler2, zug
	unentschieden = 0
	g = 0
	zug = spieler1
	if (spieltyp == 1):
		while (pruefen()):
			x = unerfahrener_zug()
			feld_markieren(x, zug)
			if (sieg()):
				unentschieden = 1 
				return zug
			wer_ist_dran()
		if (unentschieden == 0):
			return 0	

#Abrufen aller Funktionen sowie der Output

gewinne_sp1, unentschieden = spiel1(n) #Die beiden wichtigen Variabeln werden für spätere Verwendung abgespeichert
print("Gewinnchance in % des 1. Spielers mit {} Versuchen: {}\nTotale Gewinne des 1. Spielers: {}\nTotale Gewinne des 2. Spielers: {}\nTotale Unentschieden: {}\n*********************************************\nErstellt von Nikola Knezevic, Lya Marti & Simon Heller\n*********************************************".format(n,gewinne_sp1/n*100, gewinne_sp1,n-gewinne_sp1-unentschieden,unentschieden))
#Dieser print()-Befehl ist durchaus lang, jedoch ist er effizient, da er mithilfe von \n (Zeilenende) und {} (Variabeln in print()-Befehlen) die Ausgabe auf eine Zeile bringt, anstatt auf enorm viele
#Die Variabeln werden direkt im print()-Befehl ausgerechnet und aufgeruft. Da die Variabeln oben abgespeichert wurden, muss der Code nicht mehrmals durchlaufen werden. Somit lauft alles effizienter.