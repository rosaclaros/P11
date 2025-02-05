
ipa_ausschnitt = ["Nasale", "Frikative", "Approximanten", "Plosive", "Vokale"]

#Sortiere die Liste ipa_ausschnitt zuerst alphabetisch- aber rückwärts.
ipa_ausschnitt.reverse()
#Erfrage das zweite Element der Liste!
ipa_ausschnitt[1]
#Was ist das letzte Element der Liste? Welche Alternative gibt es zu [4]?
ipa_ausschnitt[-1]
#Gib die Elemente Nummer 1 bis 3 zurück.
ipa_ausschnitt[1:4]
#Füge "Vibrant" als drittes Listenelement ein!
ipa_ausschnitt.append('Vibrant')


def noten_median(x):

    sortierte_liste = sorted(x)
    laenge = len(sortierte_liste)
    
    # Überprüfe, ob die Länge der Liste ungerade ist
    if laenge % 2 == 1:
        # Bei ungerader Länge: Gib das mittlere Element zurück
        median = sortierte_liste[laenge // 2]
    else:
        # Bei gerader Länge: Berechne den Durchschnitt der beiden mittleren Elemente
        mittel1 = sortierte_liste[laenge // 2 - 1]
        mittel2 = sortierte_liste[laenge // 2]
        median = (mittel1 + mittel2) / 2
    
    return median

def flaeche_berechnen(a, b):
    flaeche = a * b
    print("Der Flächeninhalt beträgt " + str(flaeche) + ".")

import re


def passwort_ueberpruefen(passwort):

    if len(passwort) < 8:
        return "Das Passwort muss mindestens 8 Zeichen lang sein."
    if not re.search(r'[A-Z]', passwort):
        return "Das Passwort muss mindestens einen Großbuchstaben enthalten." 
    if not re.search(r'[0-9]', passwort):
        return "Das Passwort muss mindestens eine Ziffer enthalten."

    return "Das Passwort wird akzeptiert."
