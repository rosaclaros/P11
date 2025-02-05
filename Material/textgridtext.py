
import textgrids
import os


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


from textgrid import TextGrid

def get_label_durations_for_word(textgrid_file, target_word):
    # Load the TextGrid file
    tg = TextGrid.fromFile(textgrid_file)

    # Get the 'words' and 'transcription' tiers
    words_tier = tg.getFirst("words")
    transcription_tier = tg.getFirst("transcription")

    # Check if the tiers exist
    if not words_tier or not transcription_tier:
        raise ValueError("Required tiers ('words' or 'transcription') not found in the TextGrid.")

    # Iterate through intervals in the 'words' tier
    for word_interval in words_tier:
        if word_interval.mark == target_word:
            # Get the time range of the target word
            word_start = word_interval.minTime
            word_end = word_interval.maxTime

            # Find labels in the 'transcription' tier that fall within the word's time range
            label_durations = []
            for label_interval in transcription_tier:
                if (label_interval.minTime >= word_start and label_interval.maxTime <= word_end):
                    label_duration = label_interval.maxTime - label_interval.minTime
                    label_durations.append((label_interval.mark, label_duration))

            return label_durations

    # If the target word is not found
    return None

# Example usage
textgrid_file = "example.TextGrid"
target_word = "hello"
durations = get_label_durations_for_word(textgrid_file, target_word)

if durations:
    print(f"Labels and durations for the word '{target_word}':")
    for label, duration in durations:
        print(f"  Label: {label}, Duration: {duration:.3f} seconds")
else:
    print(f"The word '{target_word}' was not found in the 'words' tier.")



basisname, extension = os.path.splittext(dateiname)


