import os

#Übung 1: Urlaubsfieber


def file_or_folder():
    # Aktuelles Verzeichnis ermitteln
    aktuell = os.getcwd()
    ziel = input(f"Du bist aktuell im Verzeichnis:\n{aktuell}\nIn welches Verzeichnis möchtest du wechseln (oder drücke Enter, um hier zu bleiben)? ")
    ziel = ziel or aktuell  # Standardwert: aktuelles Verzeichnis
    pfad = os.path.realpath(ziel)

    # Prüfen, ob der Pfad existiert
    if os.path.exists(pfad):
        if os.path.isdir(pfad):  # Ordner prüfen
            print(f"'{pfad}' ist ein Ordner.")
            dateien = os.listdir(pfad)
            counter_files = 0
            counter_folders = 0

            for item in dateien:
                pfad_und_datei = os.path.join(pfad, item)
                if os.path.isfile(pfad_und_datei):
                    counter_files += 1
                elif os.path.isdir(pfad_und_datei):
                    counter_folders += 1
                else:
                    print(f"Unbekannter Typ: {pfad_und_datei}")

            print(f"Der Ordner enthält:\n- {counter_files} Datei(en)\n- {counter_folders} Ordner.")
        elif os.path.isfile(pfad):  # Datei prüfen
            print(f"'{pfad}' ist eine Datei.")
        else:
            print(f"Unbekannter Typ: '{pfad}'")
    else:
        print(f"Der Pfad '{pfad}' existiert nicht. Bitte überprüfe deine Eingabe.")


#Welche Dateien liegen im Unterordner Reservierungsbestätigungen?

def ordner_erfragen():
    aktuell = os.getcwd() #Returns the current working directory
    ziel = input(f'Du bist aktuell im Verzeichnis {aktuell}. In welches Verzeichnis möchtest du gehen? ') or aktuell
    pfad = os.path.realpath(ziel)
    if os.path.exists(pfad):
        if os.path.isdir(pfad):
            return pfad
    return None

