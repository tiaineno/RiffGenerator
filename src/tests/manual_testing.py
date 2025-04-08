"""
Using Metallica songs for manual testing
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from markov import Generator
import midi

metallica = Generator(3)

for file in os.listdir("./data/input/metallica"):
    print(f"Inserting file {file}")
    metallica.insert(midi.midi_to_list(os.path.join("./data/input/metallica", file)))

metallica_output = metallica.generate(16)
print("")
print("Random midi sequence generated with 4 metallica songs as an input:")
print(metallica_output)
midi.list_to_midi(metallica_output, "./data/output/metallica.mid")
