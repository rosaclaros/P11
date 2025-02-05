import re

def addieren(a,b):
    if a == 0:
        return b
    else:
        return 1 + addieren (a-1, b)
    
summe = addieren(17, 4)
print(summe)

def quersumme(zahl):
    anzahl = 0
    for ziffer in len(zahl):
        anzahl += len(ziffer)

        return anzahl
    

class Person:
    def __init__(self, nachname, erstervorname):
        self.name = nachname
        self.vorname = erstervorname
    
    def presentation(self):
        print(f"Hallo, mein Name ist ", self.name, " ", self.vorname)

p1 = Person("Ladegofed", "Peter")


class Student(Person):
    def __init__(self, name, erstervorname, fach):
        super().__init__(name, erstervorname)
        self.hauptfach = fach

s1 = Student("Claros", "Rosa", "Phonetik")



text = "Heute ist schone Fruhlingswetter."
ergebnis = re.split(r"s", text)
print(ergebnis)

woerter = re.split(r"\s+", text)
print(woerter)

text = "astfreie flussschiffe fahren im schritttempo"
ergebnisse = re.findall(r"[stf]{3}", text)
for fundstelle in ergebnisse:
    print(fundstelle)                
