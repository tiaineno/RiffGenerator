import sys
import os
import pytest
import shutil
from music21 import note, stream

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.midi import midi_to_list, list_to_midi

@pytest.fixture
def create_file():
    """
    create a midi file to help testing
    """
    test_input_path = './data/input/test.mid'
    test_notes = [60, 62, 64, 65, 67]

    midi_stream = stream.Stream()
    for element in test_notes:
        midi_stream.append(note.Note(element))
    midi_stream.write('midi', fp=test_input_path)

    return test_input_path, test_notes

def test_list_to_midi(create_file, cleanup_files):
    """
    test if the function saves a list as a midi file correctly
    """
    test_input_path, test_notes = create_file
    test_output_path = './data/output/testfolder/test_output.mid'

    list_to_midi(test_notes, test_output_path)

    assert os.path.exists(test_output_path)

    with open(test_output_path, 'rb') as f:
        data = f.read(4)
        assert data[:4] == b'MThd'

def test_midi_to_list(create_file, cleanup_files):
    """
    test if the function converts midi file into a list correctly
    """
    test_input_path, test_notes = create_file
    result = midi_to_list(test_input_path)
    assert result == test_notes

@pytest.fixture
def cleanup_files():
    """
    remove test files after testing
    """
    yield
    test_input_path = './data/input/test.mid'
    test_folder_path = './data/output/testfolder'

    if os.path.exists(test_input_path):
        os.remove(test_input_path)
    if os.path.exists(test_folder_path):
        shutil.rmtree(test_folder_path)
