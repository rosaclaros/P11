import textgrids
import wave
import os

grid = textgrids.TextGrid('./01_atteindre_sombre.TextGrid')
tiernames = grid.keys()
for tier in tiernames:
    print(f'{tier}')


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

def getTierNames(path):
    tiernames = []
    grid = textgrids.TextGrid(path)
    for tiername in grid:
        tiername.append(tiernames)
    return tiernames

def getTierSegmentsLabels(path, tiername):
    grid = textgrids.Textgrid(path)
    for tiername in grid:
        segments = grid[tiername]
        labels = []
        for segment in segments:
            labels.append(segment.text)
        return labels
    return None