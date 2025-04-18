# Riff Generator

The Riff Generator is a Python program that creates random midi sequences based on midi files used as an input. The program uses trie as a data structure and Markov chain to generate the riffs. The program will print the outcome and save the result as an midi file in /data/output.

## Installation and usage

Clone the repository:
```bash
git clone https://github.com/tiaineno/RiffGenerator
cd RiffGenerator
```
Install dependencies, you need to have python and poetry installed to proceed:
```bash
poetry shell
poetry install
```
Run the program with:
```bash
poetry run python src/index.py
```	

## Input parameters ##
### order
Order will determine how many previous notes the program considers when generating the next one. Smaller number will lead to more random results. 2 is a good starting point (3 with large amount of input)
### midi files
You can use the default input files when testing the program. The recommended input for testing is the folder "beatles", just type beatles in the prompt to insert the whole folder. Other default files include the folder "metallica" and the files nevergonnagiveyouup.mid and tuikituikitahtonen.mid.

You can also use your own midi-files (or folders with midi-files) by moving them in data/input. Don't forget the .mid-ending when typing single files. 
### length
Length of the midi sequence (in measures). 32 measures is usually long enough for testing.

## Output ##
The program will print out the generated melody and rhythm separately. To save the generation as a midi-file, type y and enter the file name to write. The file will be saved in data/output/(file_name.mid). You can use any midi-player to play the files, I have used https://signal.vercel.app.

## Tests and coverage ##
run tests:
```bash
poetry run pytest .
```

run coverage and generate the report:
```bash
poetry run coverage run -m pytest
poetry run coverage html
```
