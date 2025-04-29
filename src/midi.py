import os
from fractions import Fraction
from music21 import converter, note, chord, stream, meter, exceptions21

def parse_duration(duration: str) -> float:
    """
    util to help in setting the meter
    """
    duration = duration[4:]
    if '/' in duration:
        return float(Fraction(duration))
    return float(duration)

def parse_measure(measure: stream.Measure, pitches: list[int]) -> list[str]:
    """
    util which returns the rhythm of the measure and adds the pitches
    to the list

    parameters:
    measure: measure to be parsed
    notes: a list where the pitches will be added

    there is currently some inconsistency with chords;
    in some cases other than the root note will be added
    """
    for i in measure:
        if isinstance(i, stream.Voice):
            return parse_measure(i, pitches)

    bar = []
    events = sorted(measure.notesAndRests, key=lambda e: e.offset)
    for i in range(len(events)):
        element = events[i]
        dur = float(element.quarterLength)

        #this will be needed after the issue with chords is fixed
        """
        if i < len(events)-1:
            start = element.offset
            next_note = events[i+1]
            if next_note.offset < start+dur:
                dur = next_note.offset - start
        """

        if isinstance(element, note.Note):
            pitches.append(element.pitch.midi)
            bar.append(f"note{dur}")

        elif isinstance(element, chord.Chord):
            pitches.append(min(p.midi for p in element.pitches))
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
    pitches = []
    rhythms = []
    prev_empty_bar = False

    for part in midi_data.parts:
        for measure in part.getElementsByClass('Measure'):
            bar = parse_measure(measure, pitches)

            empty_bar = not any("note" in e for e in bar)
            if empty_bar and prev_empty_bar:
                continue
            prev_empty_bar = empty_bar

            rhythms.append(" ".join(bar).strip())
    return (pitches, rhythms)

def list_to_midi(seq, path):
    """
    takes a list of midi notes (seq) and writes them as a midi file in the location
    given in the second parameter (path)
    """
    melody, rhythms = seq
    midi_stream = stream.Stream()

    melody_index = 0
    for measure in rhythms:
        elements = measure.strip().split()
        measure_stream = stream.Measure()
        total_duration = 0

        for element in elements:
            duration = parse_duration(element)
            if element[:4] == "note":
                n = note.Note(melody[melody_index])
                n.quarterLength = duration
                midi_stream.append(n)
                total_duration += duration
                melody_index += 1
            elif element[:4] == "rest":
                r = note.Rest()
                r.quarterLength = duration
                midi_stream.append(r)
                total_duration += duration

        try:
            m = meter.TimeSignature(f"{int(total_duration)}/4")
            measure_stream.insert(0, m)
            midi_stream.append(measure_stream)
        except exceptions21.MeterException:
            print(f"Error with a measure with total duration of {total_duration}")

    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    midi_stream.write('midi', fp=path)
