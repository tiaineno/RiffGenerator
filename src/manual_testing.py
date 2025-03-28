"""
Using Tuiki Tuiki Tähtönen and Metallica songs for manual testing
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from markov import Generator
import midi

tuikituiki = Generator(3)
tt_midi = [48,48,55,55,57,57,55,53,53,52,52,50,50,48,55,55,53,53,52,52,50,55,55,53,53,52,52,50,
         48,48,55,55,57,57,55,53,53,52,52,50,50,48]
tuikituiki.insert(tt_midi)

mop = Generator(3)
mop_midi = [40,41,47,40,41,48,40,41,49,40,41,48,40,41,47,47,
         40,41,47,40,41,48,40,41,43,42,40,43,42,40,43,42,
         40,40,40,40,40,40,40,40,40,43,45,40,46,45,43,45,
         40,40,40,40,40,40,40,40,40,43,45,43,45]
mop.insert(mop_midi)

print("Random midi sequence generated with tuiki tuiki tähtönen as an input:")
print(tuikituiki.generate(16,48))
print("")
print("Random midi sequence generated with Master of Puppets as an input:")
print(mop.generate(16,40))

metallica = Generator(3)

for file in os.listdir("./data/input/metallica"):
    print(f"Inserting file {file}")
    metallica.insert(midi.midi_to_list(os.path.join("./data/input/metallica", file)))

metallica_output = metallica.generate(16,40)
print("")
print("Random midi sequence generated with 4 metallica songs as an input:")
print(metallica_output)
midi.list_to_midi(metallica_output, "./data/output/metallica.mid")
