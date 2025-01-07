
import os.path
import wave


def cutaudiofile(sourcefile, boundaries, targetfile):
    
    with wave.open(str(sourcefile), 'rb') as infile:
    
        params = infile.getparams()
        (left,right) = boundaries
    
        initpause = int(left * params.framerate)
        finalpause = int(right * params.framerate)
        soundframes = finalpause - initpause
    
        _= infile.readframes(initpause)
        sounddata = infile.readframes(soundframes)
    
        with wave.open(str(targetfile), 'wb') as outfile:
            outfile.setparams(params)
            outfile.setnframes = soundframes
            outfile.writeframes(sounddata)
        
            return soundframes

    return 0

directory = '../audiodateien/audiodateien'
infile = 'Test0001IT_S0.wav'
infile_path = os.path.join(directory, infile)
outfile = 'Test0001IT_S0.wav'
outfile_path = os.path.join(directory, outfile)
boundaries = [2.5, 3.27]
cutaudiofile(infile_path, boundaries, outfile_path)

    
    
    
    