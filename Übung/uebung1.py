

def vorstellen(name, fach):
    satz = f'Hallo, ich heiße {name} und studiere {fach}.'
    return satz

print(vorstellen('Rosa', 'Phonetik'))

def verdoppeln(zahl):
    verdoppelt_zahl = zahl * 2
    return verdoppelt_zahl

def bestellen(anzahl, backware):
    ausgabe = f'Ich hätte bitte gerne {anzahl} {backware}.'
    return(ausgabe)
    
print(bestellen(2, "Brezen"))

def prozent(zahl_1, zahl_2):
    rechnen = zahl_1 / 100 * zahl_2
    ausgabe = str(zahl_2) + " % von " + str(zahl_1) + " sind " + str(rechnen)
    return(ausgabe)

def harry_beziehung(person):
    if person == 'Albus Dumbledore':
        return f'Mentor'
    elif person == 'Ron Weasley':
        return f'Bester Freund'
    elif person == 'Lily Potter':
        return f'Mutter'
    else:
        return f'Keine Beziehung'
    
def durch_drei(zahl):
    if zahl % 3 == 0:
        return f'Ende!'
    else:
        durch_drei(zahl - 1)
        print(f'zahl')

    