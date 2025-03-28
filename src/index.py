"""
this is the implementation of the UI, that runs in the console
"""

import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from markov import Generator
import midi

"""
A function that will generate, print and possibly save a sequence with the given parameters
"""
def generate(generator, length, note):
    output = generator.generate(length, note)
    print("\ngenerated sequence:")
    print(output)

    save = input("\nSave the file (y/n): ")

    if save.lower() == "y":
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        midi.list_to_midi(output, f"./data/output/output{timestamp}.mid")
        print(f"saved {timestamp}.mid in ./data/output/")

"""
main loop
"""
while True:
    print("\nWelcome to the riff generator!")
    print("Start by choosing what order to use (default=3)\n")
    order = input("Order: ")
    if order == "":
        order = 3
    try:
        order = int(order)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    generator = Generator(order)

    print("\nEnter the name of a midi file or a folder with midi files, "
        "both should be located in /data/input/")
    print("Enter an empty string to generate\n")

    """
    this loop takes the inputs until the user decides to start the generation
    """
    while True:
        path = input("File or folder name: ")
        if path == "":
            if generator.trie.root.children == [None] * 128:
                print("Cannot generate with empty input")
                continue
            break
        full_path = os.path.join("./data/input/", path)

        if os.path.isdir(full_path):
            for file in os.listdir(full_path):
                if file.endswith(".mid"):
                    print(f"Inserting file {file}")
                    generator.insert(midi.midi_to_list(os.path.join(full_path, file)))
            print(f"folder {path} inserted succesfully\n")

        elif os.path.isfile(full_path):
            generator.insert(midi.midi_to_list(full_path))
            print(f"file {path} inserted succesfully\n")

        else:
            print("Invalid path. Please enter a valid file or folder\n")

    """
    this loop that will run when the user decides to use the same files after generation
    """
    while True:
        try:
            length = int(input("Length: "))
            note = int(input("Note: "))
        except ValueError:
            print("Invalid input, please enter integers")
            continue

        try:
            generate(generator, length, note)
        except IndexError:
            print("Something went wrong, the starting note is probably not in the input\n")
            continue

        """
        this loop will keep running when the user chooses the option 1
        """
        while True:
            print("\nChoose what to do next:")
            print("0 = Start over")
            print("1 = Generate again with the same settings")
            print("2 = Change settings and keep the input")

            try:
                choice = int(input("Choice: "))
            except ValueError:
                print("Invalid input. Please enter 0, 1, or 2.")
                continue

            if choice == 0 or choice == 2:
                break
            if choice == 1:
                generate(generator, length, note)
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")

        if choice == 0:
            break
