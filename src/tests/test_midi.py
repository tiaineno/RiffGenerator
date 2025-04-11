import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.midi import midi_to_list, list_to_midi

def test_list_to_midi():
    """
    test if the function saves a list as a midi file correctly
    """
    midi = [40, 41, 42, 43, 44]
    path = "data/output/test_output.mid"
    list_to_midi(midi, path)
    
    assert os.path.exists(path)

    with open(path, 'rb') as f:
        data = f.read(4)
        assert data[:4] == b'MThd'

    os.remove(path)

def test_midi_to_list():
    """
    test if the function converts midi file into two lists correctly
    """
    path = "./data/input/nevergonnagiveyouup.mid"
    result = midi_to_list(path)
    #melody
    assert result[0][:10] == [61, 61, 58, 61, 63, 60, 58, 60, 58, 56]
    #rhythm
    assert result[1][:2] == ['rest0.5 note0.25 rest0.25 note0.5 note0.5 note0.5 note0.75 rest0.75 ',
                             'rest0.5 note0.5 note0.5 note0.75 note0.25 note0.75 rest0.75 ']
