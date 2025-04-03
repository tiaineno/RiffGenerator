import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.markov import Generator
from src.midi import midi_to_list

def test_insert():
    """
    test if a sequence is inserted correctly
    """
    gen = Generator(3)
    sequence = [60, 62, 64, 65, 67, 69, 71, 72]
    gen.insert(sequence)

    assert gen.trie.find([60, 62]) == {64: 1}

def test_probs():
    """
    test if probablities are counted correctly
    """
    gen = Generator(3)
    probs = {64: 1, 65:2}
    assert gen.get_probabilities(probs) == {64:1/3, 65:2/3}
    probs_empty = {}
    assert gen.get_probabilities(probs_empty) == {}

def test_isempty():
    """
    test if isempty works correctly
    """
    gen = Generator(3)
    assert gen.isempty() is True

    sequence = [60, 62, 64, 65, 67, 69, 71, 72]
    gen.insert(sequence)
    assert gen.isempty() is False

def test_right_key():
    """
    test if all the notes exist in the input after generating with order 1
    """
    gen = Generator(1)
    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    gen.insert(sequence)

    result = gen.generate(5, 40)

    assert len(result) == 5
    assert all(note in sequence for note in result)

def test_order2():
    """
    Test if order2 works; every combination of order + 1 consecutive notes
    should be in the input
    """
    gen = Generator(2)
    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    gen.insert(sequence)

    result = gen.generate(20, 40)
    for i in range(len(result)-3):
        found = False
        """
        these loops will check if every sequence is part of input
        """
        for j in range(len(sequence)):
            if (sequence[j:j+3] == result[i:i+3] or
                sequence[j:] + sequence[:j+3-len(sequence)] == result[i:i+3]):
                    found = True
        assert found is True

def test_midi_insert():
    """
    Test if inserting (multiple) midi-files works (using order 4)
    """
    gen = Generator(4)
    sequence = midi_to_list("./data/input/metallica/mop.mid")
    sequence2 = midi_to_list("./data/input/metallica/sandman.mid")

    gen.insert(sequence)
    gen.insert(sequence2)

    result = gen.generate(20, 40)
    for i in range(len(result)-5):
        found = False
        for j in range(len(sequence)):
            if (sequence[j:j+5] == result[i:i+5] or
                sequence[j:] + sequence[:j+5-len(sequence)] == result[i:i+5] or
                sequence2[j:j+5] == result[i:i+5] or
                sequence2[j:] + sequence2[:j+5-len(sequence2)] == result[i:i+5]):
                    found = True
        assert found is True
