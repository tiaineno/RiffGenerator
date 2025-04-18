import os
from fractions import Fraction
from music21 import converter, note, chord, stream, meter

"""
util to helps in setting the meter
"""
def parse_duration(duration_str):
    duration_str = duration_str[4:]
    if '/' in duration_str:
        return float(Fraction(duration_str))
    else:
        return float(duration_str)

"""
util which returns the rhythm of the measure and adds the pitches
to the list

parameters:
measure: measure to be parsed
notes: a list where the pitches will be added

there is currently some inconsistency with chords;
in some cases other than the root note will be added
"""
def parse_measure(measure, notes):
    bar = []
    if isinstance(measure[0], stream.Voice):
        return(parse_measure(measure[0], notes))

    events = sorted(measure.notesAndRests, key=lambda e: e.offset)
    for i in range(len(events)):
        element = events[i]
        dur = float(element.quarterLength)

        #this will prevent the insertion of overlaping notes
        if i < len(events)-1:
            start = element.offset
            next_note = events[i+1]
            if next_note.offset < start+dur:
                dur = next_note.offset - start

        if isinstance(element, note.Note):
            notes.append(element.pitch.midi)
            bar.append(f"note{dur}")

        elif isinstance(element, chord.Chord):
            notes.append(min(p.midi for p in element.pitches))
            bar.append(f"note{dur}")

        elif isinstance(element, note.Rest):
            bar.append(f"rest{dur}")
    return bar


def midi_to_list(path):
    """
    Converts a given MIDI file into a tuple with two lists:
    one with the pitches and one with the rhythms, measure by measure
    consecutive empty bars wont be added
    """
    midi_data = converter.parse(path)
    notes = []
    rhythms = []
    prev_empty_bar = False

    for part in midi_data.parts:
        for measure in part.getElementsByClass('Measure'):
            bar = parse_measure(measure, notes)
            if not bar:
                continue

            empty_bar = not any("note" in e for e in bar)
            if empty_bar and prev_empty_bar:
                continue
            prev_empty_bar = empty_bar

            rhythms.append(" ".join(bar).strip())
    return (notes, rhythms)

def list_to_midi(seq, path):
    """
    takes a list of midi notes (seq) and writes them as a midi file in the location
    given in the second parameter (path)
    """
    melody, rhythms = seq
    midi_stream = stream.Stream()

    i = 0
    for measure in rhythms:
        elements = measure.strip().split()
        measure_stream = stream.Measure()
        total_duration = 0
        for element in elements:
            duration = parse_duration(element)
            if element[:4] == "note":
                n = note.Note(melody[i])
                n.quarterLength = duration
                midi_stream.append(n)
                total_duration += duration
                i += 1
            elif element[:4] == "rest":
                r = note.Rest()
                r.quarterLength = duration
                midi_stream.append(r)
                total_duration += duration
        try:
            m = meter.TimeSignature(f"{int(total_duration)}/4")
            measure_stream.insert(0, m)
        except:
            print(f"Error with a measure with total duration of {total_duration}")
        midi_stream.append(measure_stream)

    folder_path = os.path.dirname(path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    midi_stream.write('midi', fp=path)
