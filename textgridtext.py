
import textgrids


def getTierNames (filename):
    tiernames = []
    grid = textgrids.TextGrid(filename)
    for tiername in grid:
        tiernames.append(tiername)
    return tiernames

# getTierSegmentLabels() gibt eine Liste der Segmentlabel für eine bestimmte Tier zurück

def getTierSegments(filename, tiername):

    grid = textgrids.TextGrid(filename)
    if tiername in grid:
        segments = grid[tiername]
        intervals = []
        for segment in segments:
            interval = [segment.xmin, segment.text, segment.xmax]
            intervals.append(interval)
        return intervals
    return None
        


file_name = '../audiodateien/audiodateien/Test0001IT_S0.Textgrid'
tier_name = 'ORT-MAU'
segments = getTierSegments(file_name, tier_name)

