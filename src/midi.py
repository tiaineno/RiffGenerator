import os
from music21 import converter, note, chord, stream

def midi_to_list(path):
    """
    converts a given midi file into two lists:
    one with the pitches and one with the rhythms, measure by measure
    """
    midi_data = converter.parse(path)
    notes = []
    rhythms = []
    for part in midi_data.parts:
        for measure in part.getElementsByClass('Measure'):
            bar = ""
            for element in measure.notesAndRests:
                if isinstance(element, note.Note):
                    notes.append(element.pitch.midi)
                #using root notes
                if isinstance(element, chord.Chord):
                    notes.append(element.pitches[-1].midi)

                if isinstance(element, note.Rest):
                    bar += (f"rest{str(element.quarterLength)} ")
                else:
                    bar += (f"note{str(element.quarterLength)} ")
            rhythms.append(bar)
    return (notes, rhythms)

def list_to_midi(seq, path):
    """
    takes a list of midi notes and writes them as a midi file in the location
    given in the second parameter
    """
    midi_stream = stream.Stream()

    for element in seq:
        n = note.Note(element)
        midi_stream.append(n)

    folder_path = os.path.dirname(path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    midi_stream.write('midi', fp=path)
