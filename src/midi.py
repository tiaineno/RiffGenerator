import os
from music21 import converter, note, stream

def midi_to_list(path):
    """
    converts a given midi file into a list of notes and returns it
    """
    midi_data = converter.parse(path)
    notes = []

    for part in midi_data.parts:
        for element in part.flat.notes:
            if isinstance(element, note.Note):
                notes.append(element.pitch.midi)
    return notes

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
