from functions import collect_chords, merge_chords, get_chord_index
# collect chord

dirs=['0']

for name in dirs:
    collect_chords(name)

# get chord dict and counts
merge_chords()

# get chord index
get_chord_index()