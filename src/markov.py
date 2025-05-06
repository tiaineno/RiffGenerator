import sys
import os
import random

#making sure the right path is found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

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
    def __init__(self, order: int):
        self.harmony = Trie()
        self.rhythm = Trie()
        self.order = order

    def insert(self, sequence: tuple[list, list]):
        """
        Takes an tuple as an parameter
        The tuple should consist of two lists with pitches and rhythm
        Raises an error if the amount of measures or notes is less than the order
        """
        pitches = sequence[0]
        rhythm = sequence[1]

        if len(pitches) <= self.order or len(rhythm) <= self.order:
            raise ValueError("Midi seq too short")

        for i in range(len(pitches)-self.order):
            seq = pitches[i:i+1+self.order]
            self.harmony.insert(seq)
        for i in range(len(rhythm)-self.order):
            seq = rhythm[i:i+1+self.order]
            self.rhythm.insert(seq)

    def isempty(self) -> bool:
        """
        returns if the data structure is empty or not
        """
        return self.harmony.root.children == {}

    def normalize_probabilities(self, probabilities: dict) -> dict:
        """
        utility to return probablities from a dictionary of notes
        """
        total = sum(probabilities.values())
        if total == 0:
            return {}
        return {note: count / total for note, count in probabilities.items()}

    def _generate_sequence(self, length: int, trie: Trie) -> list:
        """
        generates and returns a sequence of notes/rhythms

        parameters:
        length: the amount of notes/measures
        trie: the trie that is used for generating (harmony or rhythm)
        """
        while True:
            sequence = []
            try:
                for _ in range(length):
                    probabilities = trie.find(sequence[-self.order:])
                    probabilities = self.normalize_probabilities(probabilities)

                    next = random.choices(list(probabilities.keys()),
                                            weights=probabilities.values())[0]
                    sequence.append(next)
                return sequence
            except KeyError:
                continue

    def generate(self, length: int) -> tuple[list, list]:
        """
        generates and returns a sequence based on inserted data
        takes the desired length of measures as a parameter
        """
        rhythm = self._generate_sequence(length, self.rhythm)
        notes_count = sum(r.count("note") for r in rhythm)

        melody = self._generate_sequence(notes_count, self.harmony)

        return (melody, rhythm)
