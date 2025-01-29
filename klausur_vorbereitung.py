
import math 
import random

def schokorechner(gewicht_in_gram):

    gewicht_in_kilo = gewicht_in_gram / 1000

    if gewicht_in_kilo >= 99 or gewicht_in_kilo <= 0:
        print(f"Kein gueltiges Preis moeglich.")
    else:
        preis = gewicht_in_kilo * 1.27
        #preis = math.ceil(gewicht_in_kilo * 1.27)
        #preis = round(gewicht_in_kilo * 1.27)
        return preis
    
def euroUmrechnen(euroListe, waehrung):
    euro_sum = sum(euroListe)
    dollar = 1.05
    zloty = 4.2364
    yen = 162.8081
    konvert = 0
    satz = f"{euro_sum} Euros entspricht "

    if waehrung == "dollar":
        konvert = round(euro_sum * dollar)
        return satz + f"{konvert} {waehrung}"
    elif waehrung == "zloty":
        konvert = round(euro_sum *zloty)
        return satz + f"{konvert} {waehrung}"
    elif waehrung == "yen":
        konvert = round(euro_sum * yen)
        return satz + f"{konvert} {waehrung}"
    else:
        return f"Keine gueltiges Waehrung"


def jedesNteElement(liste, start, n):
    ergebnis = []
    for index in range(start, len(liste)):
        if (index - start) % n == 0:
            ergebnis.append(liste[index])
    return ergebnis

# Aufgabe 2.2: Ohne Fallunterscheidung mit einer Schleife
def jedesNteElement2(liste, start, n):
    return [liste[i] for i in range(start, len(liste), n)]

# Aufgabe 2.3: Ohne Fallunterscheidung mit List Comprehension
def jedesNteElement3(liste, start, n):
    return [liste[i] for i in range(start, len(liste), n)]


def stundenplan(hauptfach, nebenfach):
    counter = 0
    ueberschneidungen = []
    for termin in hauptfach:

        if termin in [plan for plan in nebenfach]:
            ueberschneidungen.append(termin)
            counter += 1
    
    if counter == 0:
        return f"Juhu, keine Überschneidungen in meinem Stundenplan!"
    
    elif counter == 1 or counter == 2:
        return f"Wie blöd, es überschneiden sich Veranstaltungen zu folgenden Terminen: {ueberschneidungen}"

    elif counter > 2:
        return f"{counter} Überschneidungen im Stundenplan."
    
import random

def zahlenraten():
    counter = 3
    zahl = random.randint(1, 10)

    print(f"Sie haben {counter} Versuche")

    while counter > 0:
        geratene_zahl = int(input(f"Raten Sie ein Zahl: "))

        if geratene_zahl == zahl:
            print(f"Richtig! {geratene_zahl} war die gesuchte Zahl.")
            return
        elif geratene_zahl < zahl:
            print("Die gesuchte Zahl ist größer!")
        else:
            print("Die gesuchte Zahl ist kleiner!")

        counter -= 1

        if counter > 0:
            print(f"Sie haben noch {counter} Versuche.")

    print(f"Leider verloren! Die gesuchte Zahl war {zahl}.")

def zahlenraten2():
    counter = 3
    zahl = random.randint(1, 10)

    print(f"Sie haben {counter} Versuche")

    while counter > 0:
        geratene_zahl = int(input(f"Raten Sie ein Zahl: "))

        if geratene_zahl == zahl:
            print(f"Richtig! {geratene_zahl} war die gesuchte Zahl.")
            return
        elif geratene_zahl < zahl:
            print("Die gesuchte Zahl ist größer!")
        else:
            print("Die gesuchte Zahl ist kleiner!")

        counter -= 1

        if counter > 0:
            print(f"Sie haben noch {counter} Versuche.")

    print(f"Leider verloren! Die gesuchte Zahl war {zahl}.")

def wuerfeln(zahl):
    return random.randint(1, zahl)

def entscheidungshilfe(liste):
    
    speiseplan = []
    
    for tag in range(7):  
        zufalls_index = wuerfeln(len(liste)) - 1 
        speiseplan.append(liste[zufalls_index])
    
    return speiseplan

        

        




