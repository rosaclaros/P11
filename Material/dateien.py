
with open("zifferntabelle.txt", "rt", encoding="utf-8") as datei:
    # Initialisierung mit leerer Liste
    zeilen = []
    
    #Schleifedurchlauf: Liste aufbauen
    for zeile in datei:
        print(f"{zeile}")
        zeilen.append(zeile)
        #ziffer, ortho, sampa, ipa, = zeile.strip().split("\t")
        
        #print(f"{ziffer}: {ipa}")

print(f"Eingelesene Zeilen: {len(zeilen)}")
# os.listdir("./")

dateiname = input("Welche Datei?")

with open (dateiname, encoding="UTF-8") as datei:
    woerterbuch = {}
    # lies zunächst die Kopfzeile
    _ = datei.readline()
    # und nun lies den Rest der Datei ein
    print(_)
    print(datei)

    for zeile in datei:
        ziffer, ortho, sampa, ipa = zeile.strip().split("\t")
        woerterbuch[ortho] = (sampa, ipa)










