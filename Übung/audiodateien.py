

aktuell = os.getcwd():
neuesVerzeichnis = holeVerzeichnis(aktuell())

if neuesVerzeichnis:
    dateipfad = os.path.join(neuesVerzeichnis, audiodatei.wav)
    
    