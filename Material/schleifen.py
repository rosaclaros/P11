
import random

def wuerfeln():
    return random.randint(1, 6)

def wuerfelnNMal(n):
    for index in range(n):
        print(f"Wurf {index + 1}: {wuerfeln()} gewuerfelt.")
# wuerfelnNMal(10) =  10 mal wuerfeln, da range(0, 10)
for i in [0, 1 , 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i, "Hello World")
    
def grosseWerte (liste, schwelle) :
    ergebnis = []
    for element in liste:
        if element > schwelle:
            ergebnis.append(element)
    
    return ergebnis

def paschwuerfeln ():
    pasch = False
    while pasch == False:
        w1 = wuerfeln()
        w2 = wuerfeln()
        if w1 == w2:
            pasch = True
        else:
            print(f"{w1} ist ungleich {w2}")
    
    print(f"{w1}, {w2} ist ein Pasch")

def paschwuerfeln2():
    while True:
        w1 = wuerfeln()
        w2 = wuerfeln()
        if w1 == w2:
            print(f"{w1}, {w2} ist ein Pasch")
            return w1
        else:
            print(f"{w1}, {w2} ist ungleich")
            
def wuerfleZahlNMal (zahl, anzahl):
    wuerfe = 0
    anzahlpassend = 0
    while anzahlpassend < anzahl:
        geworfen = wuerfeln()
        if geworfen == zahl:
            anzahlpassend = anzahlpassend + 1
        wuerfe = wuerfe + 1
    return wuerfe

def elementSuchen(zusuchen, liste):
    for element in liste:
        if element == zusuchen:
            return element  
    return (f"nichts gefunden")
        