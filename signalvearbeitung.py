import textgrids
import wave
import os

# kopiert einen Ausschnitt einer quelldatei
# in eine neue Audiodatei
# von und bis sind Angaben in Sekunden
def extrahiereFragement(quelldatei, zieldatei, von, bis):
    # quelldatei öffnen
    with wave.open(quelldatei, 'rb') as audiofile:
        params = audiofile.getparams()
        framerate = audiofile.getframerate() # Parameter auslesen: framerate
        
        fromframe = int(von * framerate)          # Zeitangaben in Frames umrechnen
        tillframe = int(bis * framerate)
        framecount = int(tillframe - fromframe)
        
        audiofile.setpos(fromframe)
        
        fragementframes = audiofile.readframes(framecount)      # gehe zum Startzeitpunk in der Datei
        
        # schreibe soviele Frams aus der ersten Datei in die neue, wie notwendig
        
        with wave.open(zieldatei, 'wb') as outfile:
            outfile.setparams(params)
            outfile.setnframes = framecount
            outfile.writeframes = (fragementframes)
                

#dateiname = './NA03_SR_1_0007.TextGrid'
#grid = textgrids.TextGrid(dateiname)


extrahiereFragement('./NA03_SR_1_0007.wav','./audioFragment.wav', 1.2, 3.6)



