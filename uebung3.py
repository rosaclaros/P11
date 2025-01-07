import random

# Übung 1.1




# Übung 1.2
def vorkommen_in_liste(zahl, liste):
    
    ergebnis = []
    
    for i in range(0, len(liste)):
        
        if len(liste[i]) == zahl:
        
            ergebnis.append(i)
    
    return ergebnis

# [i for i in range(0, len(liste)) if len(liste[1]) == 4]
        
liste = ["Heute", "ist", "nicht","alle", "Tage", "ich", "komm", "wieder", "keine", "Frage"]

# Übung 1.3

def wuerfeln(n):
    random.randint(1, n)

def ratespiel(n, max):
    erraten = False
    raten_zahl = wuerfeln(n)
    counter = 1

    while counter < max:
        eingabe = int(input("Rate ein Zahl"))
        if eingabe == raten_zahl:
            return f"Du hast richtig erraten und musst {counter * 10} Cent bezahlen"  
        else:
            print(f"Falsch geraten! Du bist bei der {counter}. Versuch. Zahle {counter * 10} Cent!")   
            counter += 1     
        
    else:
        return f"Du hast in {counter} Versuche der Zahl nicht erraten. Du muss {counter * 10} Cent zahlen"
    
# Übung 1.4

meine_to_dos = ["lernen", "aufraeumen", "kochen", "lernen", "aufraeumen" ]

def entfernung(liste):
    
    neue_liste = []
    for element in liste:
        
        if element not in neue_liste:
            neue_liste.append(element)
    
    return neue_liste

# alternativ set(liste)


# Übung 2.1

urlaubsreif = {
"t-Shirts" : "ja", "Hosen" : "ja",
"Sonnencreme" : "nein", "Snacks" : "ja",
"Perso" : "nein", "Ladekabel" : "nein", "Wanderschuhe" : "ja"
}

urlaubsreif["Sonnencreme"]

a = len(urlaubsreif)











    

    

