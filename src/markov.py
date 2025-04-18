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
    Rhythm and harmony have their own trees
    """
    def __init__(self, order):
        self.harmony = Trie()
        self.rhythm = Trie()
        self.order = order

    def insert(self, sequence):
        """
        Takes a list of midi notes as a parameter and inserts every sub sequence into the tries
        Raises an error if the amount of measures and notes is less than the order
        """
        pitches = sequence[0]
        measures = sequence[1]

        if len(pitches) <= self.order and len(measures) <= self.order:
            raise ValueError("Midi seq too short")

        for i in range(len(pitches)-self.order):
            seq = pitches[i:i+1+self.order]
            self.harmony.insert(seq)
        for i in range(len(measures)-self.order):
            seq = measures[i:i+1+self.order]
            self.rhythm.insert(seq)

    def isempty(self):
        """
        returns if the data structure is empty or not
        """
        return self.harmony.root.children == {}

    def get_probabilities(self, probabilities):
        """
        utility to return probablities from a dictionary of notes
        """
        total = sum(probabilities.values())
        if total == 0:
            return {}
        return {note: count / total for note, count in probabilities.items()}

    def generate(self, length):
        """
        generates and returns a sequence based on inserted data
        takes the length of measures as a parameter
        starts the generation again if a note/bar isnt found

        after the rhythm is generated, the pitches will be generated
        separately and they will be returned as a tuple
        """
        while True:
            rhythm = []
            note_count = 0
            try:
                for _ in range(length):
                    probabilities_rhythm = self.rhythm.find(rhythm[-self.order:])
                    probabilities_rhythm = self.get_probabilities(probabilities_rhythm)

                    next_rhythm = random.choices(list(probabilities_rhythm.keys()),
                                            weights=probabilities_rhythm.values())[0]
                    note_count += next_rhythm.count("note")
                    rhythm.append(next_rhythm)
                break
            except KeyError:
                continue

        #melody generation
        while True:
            melody = []
            try:
                for _ in range(note_count):
                    probabilities = self.harmony.find(melody[-self.order:])
                    probabilities = self.get_probabilities(probabilities)

                    next_note = random.choices(list(probabilities.keys()),
                                            weights=probabilities.values())[0]

                    melody.append(next_note)
                break
            except KeyError:
                continue
        return (melody, rhythm)