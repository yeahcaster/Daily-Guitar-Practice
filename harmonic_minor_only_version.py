#!/usr/bin/env python3
from datetime import date

# ---------- Harmonic Minor Scale Dictionary ----------
harmonic_minor_scales = {
    "C":  ["C", "D", "Eb", "F", "G", "Ab", "B"],
    "G":  ["G", "A", "Bb", "C", "D", "Eb", "F#"],
    "D":  ["D", "E", "F", "G", "A", "Bb", "C#"],
    "A":  ["A", "B", "C", "D", "E", "F", "G#"],
    "E":  ["E", "F#", "G", "A", "B", "C", "D#"],
    "B":  ["B", "C#", "D", "E", "F#", "G", "A#"],
    "F#": ["F#", "G#", "A", "B", "C#", "D", "E#"],
    "C#": ["C#", "D#", "E", "F#", "G#", "A", "B#"],
    "G#": ["G#", "A#", "B", "C#", "D#", "E", "Fx"],
    "D#": ["D#", "E#", "F#", "G#", "A#", "B", "Cx"],
    "Bb": ["Bb", "C", "Db", "Eb", "F", "Gb", "A"],
    "F":  ["F", "G", "Ab", "Bb", "C", "Db", "E"]
}

def build_chord(scale, degree, chord_type):
    """Return chord tones based on harmonic minor."""
    # scale degrees wrap
    s = scale
    i = degree

    # triad tones
    root = s[i]
    third = s[(i + 2) % 7]
    fifth = s[(i + 4) % 7]
    seventh = s[(i + 6) % 7]

    if "7" in chord_type:
        return f"{root} {third} {fifth} {seventh}"
    else:
        return f"{root} {third} {fifth}"

def main():
    # ---------- Reference ----------
    reference_date = date(2025, 1, 1)
    today = date.today()
    day_index = (today - reference_date).days

    # ---------- Fixed Data ----------
    keys = [
        "A", "E", "B", "F#", "C#", "G#", "D#",
        "Bb", "F", "C", "G", "D"
    ]

    scale_focus_types = [
        "5-shape system",
        "3NPS"
    ]

    positions = [1, 2, 3, 4, 5]
    string_sets = ["EAD", "ADG", "DGB", "GBe"]
    individual_strings = ["E", "A", "D", "G", "B", "e"]

    harmonic_minor_triads = [
        "i (minor)",
        "ii° (diminished)",
        "III+ (augmented)",
        "iv (minor)",
        "V (major)",
        "VI (major)",
        "vii° (diminished)"
    ]

    seventh_chords = [
        "i min/maj7",
        "ii m7b5",
        "III maj7#5",
        "iv min7",
        "V dom7",
        "VI maj7",
        "vii dim7"
    ]

    # ---------- Daily Selections ----------
    key = keys[day_index % len(keys)]
    scale_focus = scale_focus_types[day_index % len(scale_focus_types)]
    position = positions[day_index % len(positions)]
    string_set = string_sets[day_index % len(string_sets)]
    individual_string = individual_strings[day_index % len(individual_strings)]

    chord_index = day_index % len(seventh_chords)
    chord_of_the_day = seventh_chords[chord_index]

    scale = harmonic_minor_scales[key]

    # ---------- Output ----------
    print()
    print("HARMONIC MINOR DAILY PRACTICE")
    print("----------------------------")
    print(f"Date: {today.isoformat()}")
    print(f"Key: {key} harmonic minor")
    print(f"Scale notes: {' '.join(scale)}")
    print(f"Position / Shape: {position}")
    print(f"Scale method: {scale_focus}")
    print(f"String set: {string_set}")
    print(f"Individual string: {individual_string}")
    print()

    print("Chords:")
    for i, (triad, seventh) in enumerate(zip(harmonic_minor_triads, seventh_chords)):
        root = scale[i]
        chord_notes = build_chord(scale, i, seventh)
        print(f" - ({root}) {seventh} {triad}   [{chord_notes}]")

    print()
    print("Chord of the day:")
    root = scale[chord_index]
    chord_notes = build_chord(scale, chord_index, chord_of_the_day)
    print(f" - ({root}) {chord_of_the_day}   [{chord_notes}]")

if __name__ == "__main__":
    main()
