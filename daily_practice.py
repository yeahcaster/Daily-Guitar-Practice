#!/usr/bin/env python3
import sys
from datetime import date

VALID_MODES = {"1": "harmonic_minor", "2": "natural_minor", "3": "major"}

print("Select mode:")
print("  1) Harmonic Minor")
print("  2) Natural Minor")
print("  3) Major")
choice = input("Enter 1, 2, or 3: ").strip()

if choice not in VALID_MODES:
    print("Invalid choice.")
    sys.exit(1)

MODE = VALID_MODES[choice]

# ---------- Scale Dictionaries ----------
harmonic_minor_scales = {
    "A":  ["A",  "B",  "C",  "D",  "E",  "F",  "G#"],
    "E":  ["E",  "F#", "G",  "A",  "B",  "C",  "D#"],
    "B":  ["B",  "C#", "D",  "E",  "F#", "G",  "A#"],
    "F#": ["F#", "G#", "A",  "B",  "C#", "D",  "E#"],
    "C#": ["C#", "D#", "E",  "F#", "G#", "A",  "B#"],
    "G#": ["G#", "A#", "B",  "C#", "D#", "E",  "Fx"],
    "D#": ["D#", "E#", "F#", "G#", "A#", "B",  "Cx"],
    "Bb": ["Bb", "C",  "Db", "Eb", "F",  "Gb", "A"],
    "F":  ["F",  "G",  "Ab", "Bb", "C",  "Db", "E"],
    "C":  ["C",  "D",  "Eb", "F",  "G",  "Ab", "B"],
    "G":  ["G",  "A",  "Bb", "C",  "D",  "Eb", "F#"],
    "D":  ["D",  "E",  "F",  "G",  "A",  "Bb", "C#"],
}

natural_minor_scales = {
    "A":  ["A",  "B",  "C",  "D",  "E",  "F",  "G"],
    "E":  ["E",  "F#", "G",  "A",  "B",  "C",  "D"],
    "B":  ["B",  "C#", "D",  "E",  "F#", "G",  "A"],
    "F#": ["F#", "G#", "A",  "B",  "C#", "D",  "E"],
    "C#": ["C#", "D#", "E",  "F#", "G#", "A",  "B"],
    "G#": ["G#", "A#", "B",  "C#", "D#", "E",  "F#"],
    "D#": ["D#", "E#", "F#", "G#", "A#", "B",  "C#"],
    "Bb": ["Bb", "C",  "Db", "Eb", "F",  "Gb", "Ab"],
    "F":  ["F",  "G",  "Ab", "Bb", "C",  "Db", "Eb"],
    "C":  ["C",  "D",  "Eb", "F",  "G",  "Ab", "Bb"],
    "G":  ["G",  "A",  "Bb", "C",  "D",  "Eb", "F"],
    "D":  ["D",  "E",  "F",  "G",  "A",  "Bb", "C"],
}

# G# and D# major use double-sharps, so we use their enharmonic equivalents Ab/Eb.
major_scales = {
    "A":  ["A",  "B",  "C#", "D",  "E",  "F#", "G#"],
    "E":  ["E",  "F#", "G#", "A",  "B",  "C#", "D#"],
    "B":  ["B",  "C#", "D#", "E",  "F#", "G#", "A#"],
    "F#": ["F#", "G#", "A#", "B",  "C#", "D#", "E#"],
    "C#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
    "G#": ["Ab", "Bb", "C",  "Db", "Eb", "F",  "G"],   # Ab major (enharmonic G#)
    "D#": ["Eb", "F",  "G",  "Ab", "Bb", "C",  "D"],   # Eb major (enharmonic D#)
    "Bb": ["Bb", "C",  "D",  "Eb", "F",  "G",  "A"],
    "F":  ["F",  "G",  "A",  "Bb", "C",  "D",  "E"],
    "C":  ["C",  "D",  "E",  "F",  "G",  "A",  "B"],
    "G":  ["G",  "A",  "B",  "C",  "D",  "E",  "F#"],
    "D":  ["D",  "E",  "F#", "G",  "A",  "B",  "C#"],
}

# ---------- Chord Qualities ----------
harmonic_minor_triads = [
    "i   (minor)",
    "ii° (diminished)",
    "III+(augmented)",
    "iv  (minor)",
    "V   (major)",
    "VI  (major)",
    "vii°(diminished)",
]
harmonic_minor_sevenths = [
    "i   min/maj7",
    "ii  m7b5",
    "III maj7#5",
    "iv  min7",
    "V   dom7",
    "VI  maj7",
    "vii dim7",
]

natural_minor_triads = [
    "i   (minor)",
    "ii° (diminished)",
    "III (major)",
    "iv  (minor)",
    "v   (minor)",
    "VI  (major)",
    "VII (major)",
]
natural_minor_sevenths = [
    "i   min7",
    "ii  m7b5",
    "III maj7",
    "iv  min7",
    "v   min7",
    "VI  maj7",
    "VII dom7",
]

major_triads = [
    "I   (major)",
    "ii  (minor)",
    "iii (minor)",
    "IV  (major)",
    "V   (major)",
    "vi  (minor)",
    "vii°(diminished)",
]
major_sevenths = [
    "I   maj7",
    "ii  min7",
    "iii min7",
    "IV  maj7",
    "V   dom7",
    "vi  min7",
    "vii m7b5",
]

# ---------- Build chord tones from scale degrees ----------
def build_chord(scale, degree, chord_type):
    root    = scale[degree]
    third   = scale[(degree + 2) % 7]
    fifth   = scale[(degree + 4) % 7]
    seventh = scale[(degree + 6) % 7]
    if "7" in chord_type:
        return f"{root} {third} {fifth} {seventh}"
    else:
        return f"{root} {third} {fifth}"

def main():
    reference_date = date(2025, 1, 1)
    today = date.today()
    day_index = (today - reference_date).days

    # ---------- Fixed Data ----------
    # Circle of fifths order (starting from A minor / C major)
    keys = ["A", "E", "B", "F#", "C#", "G#", "D#", "Bb", "F", "C", "G", "D"]

    scale_focus_types = ["5-shape system", "3NPS"]
    positions = [1, 2, 3, 4, 5]

    # 4 sets of 3 adjacent strings — for practicing triads across string groups
    string_sets = ["EAD", "ADG", "DGB", "GBe"]

    # All 6 strings — for practicing the scale on a single string each day
    individual_strings = ["E", "A", "D", "G", "B", "e"]

    # ---------- Select data by mode ----------
    if MODE == "harmonic_minor":
        scales   = harmonic_minor_scales
        triads   = harmonic_minor_triads
        sevenths = harmonic_minor_sevenths
        label    = "Harmonic Minor"
    elif MODE == "natural_minor":
        scales   = natural_minor_scales
        triads   = natural_minor_triads
        sevenths = natural_minor_sevenths
        label    = "Natural Minor"
    else:  # major
        scales   = major_scales
        triads   = major_triads
        sevenths = major_sevenths
        label    = "Major"

    # ---------- Daily Selections ----------
    key               = keys[day_index % len(keys)]
    scale_focus       = scale_focus_types[day_index % len(scale_focus_types)]
    position          = positions[day_index % len(positions)]
    string_set        = string_sets[day_index % len(string_sets)]
    individual_string = individual_strings[day_index % len(individual_strings)]
    chord_index       = day_index % len(sevenths)
    chord_of_the_day  = sevenths[chord_index]
    scale             = scales[key]

    # For major mode, G# and D# are spelled as Ab/Eb
    key_display = scale[0] if MODE == "major" and key in ("G#", "D#") else key

    # ---------- Output ----------
    print()
    print(f"{label.upper()} DAILY PRACTICE")
    print("-" * 32)
    print(f"Date:            {today.isoformat()}")
    print(f"Key:             {key_display} {label.lower()}")
    print(f"Scale notes:     {' '.join(scale)}")
    print(f"Position:        {position}")
    print(f"Scale method:    {scale_focus}")
    print(f"String set:      {string_set}  (3 adjacent strings — triad practice)")
    print(f"Individual str:  {individual_string}  (single-string scale practice)")
    print()
    print("Chords:")
    for i, (triad, seventh) in enumerate(zip(triads, sevenths)):
        root        = scale[i]
        chord_notes = build_chord(scale, i, seventh)
        print(f"  ({root:2})  {seventh:16}  {triad:18}  [{chord_notes}]")
    print()
    print("Chord of the day:")
    root        = scale[chord_index]
    chord_notes = build_chord(scale, chord_index, chord_of_the_day)
    print(f"  ({root:2})  {chord_of_the_day}   [{chord_notes}]")

if __name__ == "__main__":
    main()
