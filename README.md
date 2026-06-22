# Daily-Guitar-Practice
Daily harmonic minor guitar practice generator. Randomly selects a key, scale shape (3NPS or 5-position system), string set to practice triads on, and chord-of-the-day to create a structured practice routine.


# Harmonic Minor Daily Practice

A simple daily practice generator for guitar players studying the harmonic minor scale.

Each day the program generates a focused practice routine that combines:

* Harmonic minor scale study
* Position and shape work
* 3 Notes Per String (3NPS) and traditional 5-position systems
* Triad and chord-tone visualization
* String-set specific exercises
* Chord construction and harmonic analysis

The goal is to avoid "mindless scale running" and instead build a deeper understanding of the harmonic minor sound across the entire fretboard.

## Example Output

```
HARMONIC MINOR DAILY PRACTICE
----------------------------
Date: 2026-06-22
Key: C harmonic minor
Scale notes: C D Eb F G Ab B
Position / Shape: 3
Scale method: 3NPS
String set: ADG
Individual string: G

Chords:
 - (C) i min/maj7   [C Eb G B]
 - (D) ii m7b5      [D F Ab C]
 - (Eb) III maj7#5  [Eb G B D]
 - (F) iv min7      [F Ab C Eb]
 - (G) V dom7       [G B D F]
 - (Ab) VI maj7     [Ab C Eb G]
 - (B) vii dim7     [B D F Ab]

Chord of the day:
 - (Ab) VI maj7     [Ab C Eb G]
```

## Daily Practice Workflow

When the program generates a routine:

1. Play the assigned harmonic minor scale.
2. Focus on the selected position or shape.
3. Practice within the assigned system (3NPS or 5-position).
4. Play triads and arpeggios on the designated string set.
5. Locate scale tones on the highlighted individual string.
6. Study and visualize the diatonic chords.
7. Spend extra time on the "Chord of the Day."
8. Improvise or create short musical phrases using the day's material.

## Harmonic Minor Harmony

The generator includes the seven diatonic seventh chords found in harmonic minor:

| Degree | Chord Type |
| ------ | ---------- |
| i      | min/maj7   |
| ii     | m7b5       |
| III    | maj7#5     |
| iv     | min7       |
| V      | dom7       |
| VI     | maj7       |
| vii    | dim7       |

Studying these chords helps connect scale patterns to real harmonic applications.

## Scale Shapes

The program supports:

* 3 Notes Per String (3NPS) patterns
* Traditional 5-position box patterns

The exact fretboard diagrams are not included in this repository. Any harmonic minor fingering system may be used, but the project was originally built around the shapes available here:

https://www.guitar-chords.org.uk/guitarscales/c-harmonic-minor-scale.html

## Why This Exists

Many guitar players practice scales without ever connecting them to:

* Chords
* Arpeggios
* String sets
* Harmonic function
* Fretboard visualization

This tool creates a daily prompt that forces attention onto different aspects of the harmonic minor scale, helping build practical musical knowledge rather than just finger memory.

## Future Ideas

* Melodic minor support
* Major scale modes
* Arpeggio-specific days
* Chord progression generation
* Interval training
* Fretboard note quizzes
* CSV or calendar export
* Practice history tracking
