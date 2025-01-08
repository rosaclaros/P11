
import os
import os.path

#Übung 1: Urlaubsfieber




#Welche Daten liegen in diesem Ordner? Bestimme, ob es sich dabei um Files oder Ordner handelt.

def file_or_folder():
    aktuell = os.getcwd()
    ziel = input(f"Du bist aktuell im Verzeichnis {aktuell}. In welches Verzeichnis moechtest du gehen?") or aktuell
    pfad = os.path.realpath(ziel)

    if os.path.exists(pfad):        #checks if path exists
        if os.path.isdir(pfad):           #check if path is a folder  
            dateien = os.listdir(pfad)      # saves all the files in the folder in a variable
            counter_files = 0
            counter_folders = 0
            for item in dateien:               

                pfad_und_datei = os.path.join(pfad, item)   #Path to file within file
                if os.path.isfile(pfad_und_datei):          #checks if it's a file
                    counter_files += 1
                    print(f"{item} ist eine Datei.")
                elif os.path.isdir(pfad_und_datei):         #checks if it's folder
                    counter_folders += 1
                    print(f"{item} ist ein Ordner.")
                else:
                    print(f"Weiss nicht was das ist...")
                    
            print(f"Ordner enthält {counter_files} Dateien und {counter_folders} Ordner")
            
        elif os.path.isfile(pfad):
            print(f'Es ist ein File kein Ordner.')

        else:
            print(f"Weiss nicht was das ist...")
    else:
        print(f"Pfad existier nicht.")            


#Welche Dateien liegen im Unterordner Reservierungsbestätigungen?

def ordner_erfragen():
    aktuell = os.getcwd() #Returns the current working directory
    ziel = input(f'Du bist aktuell im Verzeichnis {aktuell}. In welches Verzeichnis möchtest du gehen? ') or aktuell
    pfad = os.path.realpath(ziel)
    if os.path.exists(pfad):
        if os.path.isdir(pfad):
            return pfad
    else:    
        return None

# find all wav files without including full path
def verzeichnis_erfragen():
    aktuell = os.getcwd()
    root = aktuell
    for aktuell, verzeichnisse, dateien in os.walk(root):
        for datei in dateien:
            if datei.endswith('.wav'):
                
                dateipfad = os.path.join(aktuell, datei)
               
                print(f'{dateipfad}')
                
#??

def suchen_extension(root, ext):
    gefunden = []
    for pfad, verzeichnis, dateien in os.walk(root):
        for datei in dateien:
            if datei.endswith(ext):
                dateipfad = os.path.join(pfad, datei)
                gefunden.append(dateipfad)
    # Rückgabe der Ergebnis
    return gefunden

#alternativ

def suchen_extension(root, ext):
    gefunden = []
    for pfad, verzeichnis, dateien in os.walk(root):
        for datei in dateien:
            _, dateitext = os.path.splitext(datei)
            if ext == dateitext:
                dateipfad = os.path.join(pfad, datei)
                gefunden.append(dateipfad)
    # Rückgabe der Ergebnis
    return gefunden

#Welche Dateien liegen im Unterordner Reservierungsbestätigungen?
    
def datei_suchen(datei_name, wurzel):
    for root, dirs, files in os.walk(wurzel):
        print(f'Root: {root}, Ordner: {dirs}, Dateien: {files}.')
        
        for file in files:
            if file == datei_name:
                return os.path.join(root, file)
    return None 

#Lies die Datei Sehenswürdigkeiten.txt aus und speichere alle Sehenswürdigkeiten in einer Liste ab.        

def datei_drucken(datei_name):
    with open(datei_name, "rt", encoding="UTF8") as datei:
        zeilen = []
        for zeile in datei:
            zeilen.append(zeile.strip())
        return zeilen
    

#Lösche die Datei Tagebuch.txt  
                        
                
wurzel = ordner_erfragen()
if wurzel:
    
    x = datei_suchen("Sehenswürdigkeiten.txt", wurzel)
    liste = datei_drucken(x)

#Übung 2: Zugriff auf Audiodateien

import textgrids

def getTiersAsTexts(directory, filename):
    
    full_path = os.path.join(directory, filename)


    if not os.path.exists(full_path):
        raise FileNotFoundError(f"The file {full_path} does not exist.")

    grid = textgrids.TextGrid(full_path)
    tiers = {}  

    for tier_name in grid:
        tiertext = ""
        for segment in grid[tier_name]:
            tiertext += segment.text + " "
        tiers[tier_name] = tiertext.strip()
    
    return tiers


import wave

directory = r"C:\Users\rosac\OneDrive\Desktop\P11_Python\Übung\audiodateien"
filename = 'Test0001IT_S0.wav'
full_path = os.path.join(directory, filename)


with wave.open(full_path, 'rb') as audiofile:
    params = audiofile.getparams()
    print(params[2])
    print(params.framerate)
    

def playtime(audiofile):
    
    wav_file = wave.open(audiofile, 'r')
    frames = wav_file.getnframes()
    rate = wav_file.getframerate()
    wav_file.close() 
    duration = frames / rate
    return f'{duration} Seconds'

def totalPlaytime(directory):
    
    total_duration = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):  # Only process .wav files
                full_path = os.path.join(root, file)
                total_duration += playtime(full_path)
    return total_duration

#Übung 3 Reguläre Ausdrücke


    





               
                



   