import random

# Übung 1.1 

def haefigkeit_zaehlen(liste, suchen):
    counter = 0 
    for element in liste:
        if element == "a":
            counter += 1

    return counter


# Übung 1.2

def vorkommen_in_liste(zeichenanzahl, liste):
    ergebnis = []
    for element in range(0, len(liste)):  #range() element is not the actual element but the indice
        if len(liste[element]) == zeichenanzahl:
            ergebnis.append(element)
    return ergebnis

# [i for i in range(0, len(liste)) if len(liste[1]) == 4]
        
liste = ["Heute", "ist", "nicht","alle", "Tage", "ich", "komm", "wieder", "keine", "Frage"]

# Übung 1.3

def wuerfeln(n):
    random.randint(1, n)

def ratespiel(n, max):
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

# meine = set(meine_to_dos)

# Übung 2.1

urlaubsreif = {
"t-Shirts" : "ja", "Hosen" : "ja",
"Sonnencreme" : "nein", "Snacks" : "ja",
"Perso" : "nein", "Ladekabel" : "nein", "Wanderschuhe" : "ja"
}

urlaubsreif["Sonnencreme"]

a = len(urlaubsreif)\

aussaatplan = {
 "Frühling" : ["Rote Beete", "Brokkoli", "Erbsen"],
 "Sommer" : ["Radieschen", "Gelbe Rüben", "Tomaten", "Gurken"],
 "Herbst" : ["Zwiebeln", "Kohlrabi", "Blaubeeren"],
 "Winter" : ["Kresse", "Spinat", "Feldsalat"]
 }

aussaatplan.keys()


#Überprüfe, ob "Sonnencreme" auf der Packliste steht
urlaubsreif["Sonnencreme"]

#Du packst den Perso ein. Ändere das Dictionary dementsprechend ab!
urlaubsreif["Person"] = ["Ja"]
#Schreibe "Sonnenbrille" auf die Packliste. Der dazugehörige Value ist "ja".

urlaubsreif["Sonnenbrille"] = ["Ja"]

#Anstelle der Wanderschuhe möchtest Du doch lieber Flipflops einpacken. Schreibe die Packliste entsprechend um!

urlaubsreif["Flipflops"] = urlaubsreif["Wanderschuhe"]

#Wie viele Gegenstände stehen auf deiner Liste?

len(urlaubsreif.keys())

#Überprüfe, ob es außer ja und nein noch andere Values gibt

urlaubsreif.items()








    

    

