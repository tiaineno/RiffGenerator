import sys
import os
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

"""
making sure the right path is found
"""
try:
    from trie import Trie
except ModuleNotFoundError:
    from src.trie import Trie

class Generator:
    """
    The implementation of the riff generator
    Takes the order of a markovs chain as a parameter and creates its data structure
    """
    def __init__(self, order):
        self.trie = Trie()
        self.order = order

    def insert(self, sequence):
        """
        Takes a list of midi notes as a parameter and inserts every sub sequence into the trie
        In the end the of the input the missing notes are taken from the beginning
        """
        for i in range(len(sequence)):
            if i < len(sequence)-self.order:
                seq = sequence[i:i+1+self.order]
            else:
                seq = sequence[i:] + sequence[:i+1+self.order-len(sequence)]
            self.trie.insert(seq)

    def isempty(self):
        """
        returns if the data structure is empty or not
        """
        return self.trie.root.children == [None] * 128

    def get_probabilities(self, probabilities):
        """
        utility to return probablities from a dictionary of notes
        """
        total = sum(probabilities.values())
        if total == 0:
            return {}
        return {note: count / total for note, count in probabilities.items()}

    def generate(self, length, starting_note):
        """
        generates and returns a sequence based on inserted data
        takes the length of the sequence and the starting note as parameters
        """
        sequence = [starting_note]
        for _ in range(length-1):
            if len(sequence) < self.order:
                probabilities = self.trie.find(sequence)
            else:
                probabilities = self.trie.find(sequence[-self.order:])
            probabilities = self.get_probabilities(probabilities)
            next_note = random.choices(list(probabilities.keys()),
                                       weights=probabilities.values())[0]
            sequence.append(next_note)
        return sequence
