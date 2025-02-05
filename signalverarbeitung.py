import textgrids
import os
import os.path
import wave

# extrahiereFragment kopiert einen Ausschnitt einer Audiodatei
# in eine neue Audiodatei
# von und bis sind Angaben in Sekunden
def extrahiereFragment (quelldatei, zieldatei, von, bis):
    # audiodatei öffnen
    with wave.open(quelldatei, 'rb') as audiofile:
        # Parameter auslesen: framerate
        params = audiofile.getparams()
        framerate = params.framerate

        # Zeitangaben in Frames umrechnen
        vonframe = int(von * framerate)
        bisframe = int(bis * framerate)
        anzahlframes = int(bisframe - vonframe)

        # gehe zum Startzeitpunkt in der Datei
        audiofile.setpos(vonframe)

        # lies soviele Frames wie gewünscht ein
        fragmentframes = audiofile.readframes(anzahlframes)

        # schreibe diese Frames in die neue Datei
        with wave.open(zieldatei, 'wb') as fragmentdatei:
            fragmentdatei.setparams(params)
            fragmentdatei.writeframes(fragmentframes)

# sucht auf der Ebene tiername nach einem Segment mit einem bestimmten Label
def sucheSegmentNachLabel(tier, label):
    return [segment for segment in tier if segment.text == label]

# segementliste = sucheSegmentNachLabel('ORT-MAU', grid,'Bundeskanzler')
    
# sucht auf der Ebene Tiername nach allen Segmenten innerhalb eines Zeitraums

def sucheSegmenteImZeitraum (tier, von, bis):
    return [segment for segment in tier if (segment.xmin >= von and segment.xmax <= bis)]

#sucht auf der Ebene tiername nach einer Folge von Labeln

def sucheSegementNachLabelfolge(tier, folge):
    if len(tier) == 0:
        return None
    elif len(folge) == 0:
        return []
    elif tier[0] == folge[0]:
        return [tier[0]].append(sucheSegementNachLabelfolge(tier[1:], folge[1:]))
    else:
        return sucheSegementNachLabelfolge(tier[1:], folge)
            

# TextGrid einlesen
dateiname = './NA03_SR_1_0007.TextGrid'
grid = textgrids.TextGrid(dateiname)

# Aufgabe: schreibe jedes orthographische Wort (d.h. in der Ebene 'ORT-MAU') in eine eigene Audiodatei.

basisname, extension = os.path.splitext(dateiname)
quelldatei = f'{basisname}.wav'
tier_name = 'ORT-MAU'
# grid dictonary von Tier asl Key, Values: Liste (Intervall or Point)

# grid
zähler = 0
for element in grid[tier_name]:
    von = element.xmin
    bis = element.xmax
    
    # keine Dateien für leere Segmente anlegen!
    if len(element.text.strip()) > 0:
        # element.text enthält mindestens ein Zeichen
        zähler += 1
        print(f'{zähler}\t{element.text}\t{von}\t{bis}\t{bis-von}')

        ausgabedatei = f'{basisname}_{zähler}.wav'
        extrahiereFragment(quelldatei, ausgabedatei, von, bis)
