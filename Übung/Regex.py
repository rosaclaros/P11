#Uebung 3 Regex

import re

def passwort_ueberprufen():
    passwort = input(f'Geben Sie ein Passwort ein')
    pruefen = re.search(".{8}")

    if pruefen:
        return "Passwort gueltig!"
    else:
        return "Passwort nicht gueltig!"
    
