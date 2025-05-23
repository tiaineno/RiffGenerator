import sys
import os
import shutil

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.midi import midi_to_list, list_to_midi

def test_midi_to_list():
    """
    test if the function converts midi file into two lists correctly
    """
    path = "./data/input/major/letitbe.mid"
    result = midi_to_list(path)
    #melody
    assert result[0][:10] == [52, 52, 52, 52, 54, 49, 52, 52, 57, 59]
    #rhythm
    assert result[1][:2] == ['rest4.0', 'rest3.5 note0.25 note0.25']

def test_list_to_midi():
    """
    test if the function saves a list as a midi file correctly
    """
    melody = [61, 61, 61, 58, 61, 63, 60, 58, 60, 58, 56]
    rhythm = ['rest0.5 note0.25 rest0.25 note1/3 note1/3 note1/3 note0.5 note0.75 rest0.75',
              'rest0.5 note0.5 note0.5 note0.75 note0.25 note0.75 rest0.75']
    sequence = (melody, rhythm)

    path = "data/output/test/test_output.mid"
    list_to_midi(sequence, path)

    assert os.path.exists(path)

    with open(path, 'rb') as f:
        data = f.read(4)
        assert data[:4] == b'MThd'

    result = midi_to_list(path)

    assert result[0] == melody
    assert result[1][1] == rhythm[1]

    shutil.rmtree("data/output/test")

def test_voice():
    """
    test for a special occasion where the notes of a chord have
    different durations
    """
    result = midi_to_list("data/input/test_ukkonooa.mid")
    path = "data/output/test/ukko.mid"
    list_to_midi(result, path)
    assert result[0] == [48, 48, 48, 52, 50, 50, 50, 53,
                         52, 52, 50, 50, 48]
    assert result[1] == ['note1.0 note1.0 note1.0 note1.0',
                         'note1.0 note1.0 note1.0 note1.0',
                         'note1.0 note1.0 note1.0 note1.0',
                         'note3.0 rest1.0']
    shutil.rmtree("data/output/test")

def test_nonexistent_bar(capfd):
    """
    test if the empty bars are not added
    """
    melody = [61]
    rhythm = ['rest4.0', 'rest0.0', 'note4.0']
    sequence = (melody, rhythm)

    path = "data/output/test/test_output.mid"
    list_to_midi(sequence, path)

    out = capfd.readouterr()[0]
    assert "Error with a measure with total duration of 0.0" in out

    shutil.rmtree("data/output/test")
