import sys
import os
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.markov import Generator

def test_insert():
    gen = Generator(3)
    sequence = [60, 62, 64, 65, 67, 69, 71, 72]
    gen.insert(sequence)

    assert gen.trie.find([60, 62]) == {64: 1}

def test_probs():
    gen = Generator(3)
    probs = {64: 1, 65:2}
    assert gen.get_probabilities(probs) == {64:1/3, 65:2/3}

def test_order1():
    gen = Generator(1)
    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    gen.insert(sequence)

    result = gen.generate(5, 40)

    assert len(result) == 5
    assert all(note in sequence for note in result)

def test_order3():
    """
    Using a seed to test a special occasion which used to cause errors
    """
    gen = Generator(3)
    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    gen.insert(sequence)

    random.seed(1)
    result = gen.generate(20, 40)

    assert result == [40, 41, 43, 40, 41, 40, 41, 43, 40, 41, 40, 42, 43, 43, 43, 40, 40, 41, 42, 43]
