
# globale Variablen sind außerhalb von Funktionen definiert
def lmumail (vorname, nachname):
    links = vorname + "." + nachname 
    rechts = "campus.lmu.de"
    mail = links + "@" + rechts # das sind lokale Variablen
    return (mail)               # lokale variablen werden immer globale Variable mit gleichen Name überschrieben

print(lmumail("Max", "Mustermann"))

print("--------")

neuMail = lmumail("Christoph", "Draxler")
print(neuMail)
