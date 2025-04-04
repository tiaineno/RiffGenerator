import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from markov import Generator
import midi

class RiffGenerator:
    """
    this is the implementation of the UI, that runs in the console
    """
    def __init__(self):
        self.generator = None
        self.length = None
        self.starting_note = None

    def start(self):
        """
        takes order from the user and initializes the generator
        """
        print("Start by choosing what order to use")
        while True:
            try:
                order = int(input("Order: "))
                if order>0:
                    break
                print("Order must be atleast 1.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        self.generator = Generator(order)

    def input(self):
        """
        takes and inserts midi files and folders from the user
        """
        while True:
            path = input("File or folder name: ")
            if path == "":
                if self.generator.isempty():
                    print("Cannot generate without any input.")
                    continue
                break
            full_path = os.path.join("./data/input/", path)

            if os.path.isdir(full_path):
                for file in os.listdir(full_path):
                    if file.endswith(".mid"):
                        print(f"Inserting file {file}")
                        self.generator.insert(midi.midi_to_list(os.path.join(full_path, file)))
                print(f"Folder {path} succesfully inserted")
            elif os.path.isfile(full_path):
                self.generator.insert(midi.midi_to_list(full_path))
                print(f"File {path} succesfully inserted")
            else:
                print("Invalid path. Please enter a valid file or folder.")

    def generate(self):
        """
        A function that will generate, print and possibly save a sequence with the given parameters
        """
        output = self.generator.generate(self.length, self.starting_note)
        print("generated sequence:")
        print(output)

        save = input("Save the file (y/n): ")

        if save.lower() == "y":
            name = input("file name: ")
            midi.list_to_midi(output, f"./data/output/{name}.mid")
            print(f"saved {name}.mid in ./data/output/")

    def run(self):
        """
        runs the ui loop
        """
        print("Welcome to the riff generator!")
        while True:
            self.start()

            print("Give the midi files or a folder located at the correct input folder, "
            "enter to generate")
            self.input()

            while True:
                try:
                    self.length = int(input("Length: "))
                    self.starting_note = int(input("Note: "))
                except ValueError:
                    print("Invalid input. Please enter integers for length and note.")
                    continue

                try:
                    self.generate()
                except IndexError:
                    print("Something went wrong, try a different starting note.")
                    continue

                while True:
                    print("Choose what to do next:")
                    print("0 = Start over")
                    print("1 = Generate again with the same settings")
                    print("2 = Change settings and keep the input")

                    try:
                        choice = int(input("Choice: "))
                    except ValueError:
                        print("Invalid input. Please enter 0, 1, or 2.")
                        continue

                    if choice in (0, 2):
                        break
                    if choice == 1:
                        self.generate()
                    else:
                        print("Invalid choice. Please enter 0, 1, or 2.")

                if choice == 0:
                    break
