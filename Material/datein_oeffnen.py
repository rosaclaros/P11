
import os.path
import os


aktuell = os.getcwd()
ziel = input(f'Du bist aktuell im Verzeichnis {aktuell}. In welches Verzeichnis m¨ochtest Du gehen?') or aktuell

pfad = os.path.realpath(ziel) # konvertiert einen relativen in einen absoluten Pfad
# Python assumes that the path starts with the current working directory 

if os.path.exists(pfad): # existiert dieser Pfad?
    if os.path.isdir(pfad): # verweist der Pfad auf ein Verzeichnis?
        dateien = os.listdir(pfad) #  gibt die Dateien im Verzeichnis als Liste zurück
        print(f'Dateien im Verzeichnis {pfad}: {dateien}')
    elif os.path.isfile(pfad): #  verweist der Pfad auf eine Datei
        print(f'{pfad} ist eine Datei, kein Verzeichnis.')
    else:
        print(f'{pfad} ist weder Datei noch Pfad.')
else:
    print(f'Fehler: {pfad} ist kein gültiger Pfad.')




