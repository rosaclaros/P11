def bartSimpson(n, text):
    if n == 0:
        print("Fertig!")
    else:
        print(text)
        bartSimpson(n-1, text) # wir rufen der Funktion wieder auf bis n == 0 
    
bartSimpson(10, "ich muss meine Hausaufgaben machen!")


def fakultät(n):   # wie viele Anordnungsmöglichkeiten gibt es
    if n == 0:
        return 1
    else:
        return n * fakultät(n-1)
    
def enthält(position, liste, gesucht):
    if position >= len(liste):
        return False
    elif liste[position] == gesucht:
        return True
    else:
        return enthält(position + 1, liste, gesucht)

def woist(position, liste, gesucht):
    if position >= len(liste):
        return -1
    elif liste[position] == gesucht:
        return position
    else:
        return woist(position + 1, liste, gesucht)

def suchen(liste, gesucht):
    if len(liste) == 0:
        return False
    elif liste[0] == gesucht:
        return True
    else:
        return suchen(liste[1:], gesucht)
    
abba = ["Agnetha", 1951, "Björn", 1945, "Benny", 1946,
 "Anni-Frid", 1945]

 # 1) Kopf
def addieren (a, b):
    if a == 0:
        return b
    else:
        return 1 + addieren (a-1, b) 
    
summe = addieren(17, 4)
print(f'Die Summe ist {summe}')


def summiere(von, bis):
    if von > bis:  # Basisfall: Kein Intervall mehr
        return 0
    else:  # Rekursiver Schritt: Addiere `von` und rufe die Funktion mit `von + 1` auf
        return von + summiere(von + 1, bis)
    
print(summiere(1, 5))
# quersumme = digit sum
def quersumme(n):
    if n == 0:  # Basisfall: Keine Ziffern mehr
        return 0
    else:  # Rekursiver Schritt: Addiere die letzte Ziffer und rufe die Funktion mit dem Rest auf
        return n % 10 + quersumme(n // 10)  
        # % 10 returns last digit of number 
        # //  removes last digit
    
print(quersumme(1234))

def enthaeltZeichen(kette, zeichen):
    if not kette:  # Basisfall: Leere Zeichenkette
        return False
    elif kette[0] == zeichen:  # Prüfen, ob das erste Zeichen übereinstimmt
        return True
    else:  # Rekursiver Schritt: Prüfe den Rest der Zeichenkette
        return enthaeltZeichen(kette[1:], zeichen)
    #[1:] removes kette[0]
    
print(enthaeltZeichen("Hallo", "a"))  # Ergebnis: True
print(enthaeltZeichen("Hallo", "z"))  # Ergebnis: False

def enthaeltTeilstring(kette, teil):
    if len(kette) < len(teil):  # Basisfall: `kette` ist kürzer als `teil`
        return False
    elif kette[:len(teil)] == teil:  # Prüfen, ob der Anfang von `kette` mit `teil` übereinstimmt
        return True
    else:  # Rekursiver Schritt: Prüfe den Rest der Zeichenkette
        return enthaeltTeilstring(kette[1:], teil)
    
print(enthaeltTeilstring("Hallo Welt", "Welt"))  # Ergebnis: True
print(enthaeltTeilstring("Hallo Welt", "Welt!"))  # Ergebnis: False