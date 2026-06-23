# Daily Guitar Practice Generator

A daily practice generator for guitar players who want to study scales with harmonic context, not just run patterns up and down the neck.

Each day the program generates a focused routine combining:

* Scale study
* Position work
* Triad visualization
* Chord analysis
* Fretboard navigation

Three scale types are supported:

* Harmonic Minor
* Natural Minor
* Major

---

## Usage

Run this in a command prompt/ terminal/ windows powershell/ etc
```bash
python daily_practice.py
```
alt example:
```bash
 py .\downloads\daily_practice.py
```

You'll be prompted to select a mode:

```text
Select mode:
  1) Harmonic Minor
  2) Natural Minor
  3) Major

Enter 1, 2, or 3:
```

---

## Example Output

```text
HARMONIC MINOR DAILY PRACTICE
--------------------------------
Date:            2026-06-22
Key:             C harmonic minor
Scale notes:     C D Eb F G Ab B
Position:        3
Scale method:    3NPS
String set:      ADG
Individual str:  G

Chords:
  (C )  i   min/maj7      i   (minor)         [C Eb G B]
  (D )  ii  m7b5          ii° (diminished)    [D F Ab C]
  (Eb)  III maj7#5        III+ (augmented)    [Eb G B D]
  (F )  iv  min7          iv  (minor)         [F Ab C Eb]
  (G )  V   dom7          V   (major)         [G B D F]
  (Ab)  VI  maj7          VI  (major)         [Ab C Eb G]
  (B )  vii dim7          vii° (diminished)   [B D F Ab]

Chord of the day:
  (Ab)  VI  maj7   [Ab C Eb G]
```

---

## Daily Practice Workflow

When the program generates a routine:

1. Play the assigned scale in the selected position.
2. Focus on the selected system (3NPS or 5-position).
3. Practice triads on the assigned string set.
4. Locate and play the scale on the assigned individual string.
5. Study the diatonic chord chart-name, quality, and chord tones.
6. Spend extra time on the Chord of the Day.
7. Improvise short phrases using the day's material.

---

## How the Cycling Works

All selections are derived from the calendar date, so each day generates a new assignment without randomness.

* Running the program twice on the same day produces identical output.
* Keys cycle through the circle of fifths.
* The key order is inspired by the scale sequence popularized by Andrés Segovia, which organizes scale practice by traversing the circle of fifths rather than moving chromatically.
* Key centers repeat every 12 days.
* Position, string set, and individual string rotate on independent schedules.

The result is broad coverage of the fretboard and harmonic material over time while maintaining a consistent daily structure.

---

## Scale Modes and Harmony

### Harmonic Minor

The raised 7th creates a dominant V chord, giving harmonic minor its characteristic tension and resolution.

| Degree | Triad      | 7th Chord |
| ------ | ---------- | --------- |
| i      | minor      | min/maj7  |
| ii°    | diminished | m7b5      |
| III+   | augmented  | maj7#5    |
| iv     | minor      | min7      |
| V      | major      | dom7      |
| VI     | major      | maj7      |
| vii°   | diminished | dim7      |

### Natural Minor

| Degree | Triad      | 7th Chord |
| ------ | ---------- | --------- |
| i      | minor      | min7      |
| ii°    | diminished | m7b5      |
| III    | major      | maj7      |
| iv     | minor      | min7      |
| v      | minor      | min7      |
| VI     | major      | maj7      |
| VII    | major      | dom7      |

### Major

| Degree | Triad      | 7th Chord |
| ------ | ---------- | --------- |
| I      | major      | maj7      |
| ii     | minor      | min7      |
| iii    | minor      | min7      |
| IV     | major      | maj7      |
| V      | major      | dom7      |
| vi     | minor      | min7      |
| vii°   | diminished | m7b5      |

---

## Scale Shapes

The program supports:

* 3 Notes Per String (3NPS)
* Traditional 5-position box patterns

Fingering diagrams are not included. Any standard scale reference may be used.

The project was originally built around the harmonic minor shapes available at:

https://www.guitar-chords.org.uk/guitarscales/c-harmonic-minor-scale.html

---

## Why This Exists

Scale practice without harmonic context often builds finger memory without developing musical understanding.

This tool forces daily attention onto different aspects of the fretboard by connecting:

* Scales
* Chords
* Arpeggios
* String groups
* Harmonic function
* Fretboard visualization

The goal is to move beyond pattern memorization and build a practical understanding of how scales and harmony relate.

---
