import sys
import os
import random
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.markov import Generator
from src.midi import midi_to_list

melody = [61, 61, 58, 61, 63, 60, 58, 60, 58, 56]
rhythm = ['rest0.5 note0.25 rest0.25 note0.5 note0.5 note0.5 note0.75 rest0.75',
          'rest0.5 note0.5 note0.5 note0.75 note0.25 note0.75 rest0.75',
          'rest0.5 note0.25 rest0.25 note0.5 note0.5 note0.5 note0.75 rest0.75',
          'rest4.0']
sequence = (melody, rhythm)

def test_insert():
    """
    test if a sequence is inserted correctly
    """
    gen = Generator(2)
    gen.insert(sequence)

    assert gen.harmony.find([60, 58]) == {56: 1, 60: 1}
    assert gen.rhythm.find([
        'rest0.5 note0.25 rest0.25 note0.5 note0.5 note0.5 note0.75 rest0.75',
        'rest0.5 note0.5 note0.5 note0.75 note0.25 note0.75 rest0.75'
    ]) == {
        'rest0.5 note0.25 rest0.25 note0.5 note0.5 note0.5 note0.75 rest0.75': 1
    }

def test_insert_too_short():
    """
    Test if the class handles too short midi seqs correctly
    """
    gen = Generator(12)
    with pytest.raises(ValueError):
        gen.insert(sequence)

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

    gen.insert(sequence)
    assert gen.isempty() is False

def test_seed():
    """
    testing a specific situation where the generation is started again
    with rhythm and melody
    """
    random.seed = 0
    gen = Generator(1)
    gen.insert(sequence)
    gen.generate(8)
    assert gen.isempty() is False

def test_right_key():
    """
    test if all the notes exist in the input after generating with order 1
    """
    gen = Generator(1)
    gen.insert(sequence)
    result = gen.generate(3)
    assert len(result[1]) == 3
    assert all(note in melody for note in result[0])
    assert all(bar in rhythm for bar in result[1])

def result_checker(seq, result, order):
    """
    checks if every subseq of the result is part of the input
    """
    order += 1
    for i in range(len(result)-order):
        found = False
        for j in range(len(seq)-order):
            if seq[j:j+order] == result[i:i+order]:
                found = True
        assert found is True

def test_order2():
    """
    Test if order2 works; every combination of order + 1 consecutive notes
    should be in the input
    """
    gen = Generator(2)
    sequence2 = midi_to_list("./data/input/nevergonnagiveyouup.mid")
    gen.insert(sequence2)
    result = gen.generate(16)

    result_checker(sequence2[0], result[0], 2)
    result_checker(sequence2[0], result[0], 2)

def test_multiple_insert():
    """
    Test if inserting (multiple) midi-files works (using order 3)
    """
    gen = Generator(3)
    sequence3 = midi_to_list("./data/input/beatles/letitbe.mid")
    sequence4 = midi_to_list("./data/input/beatles/blackbird.mid")

    gen.insert(sequence3)
    gen.insert(sequence4)

    result = gen.generate(20)

    result_checker(sequence3[0] + sequence4[0], result[0], 3)
    result_checker(sequence3[1] + sequence4[1], result[1], 3)
