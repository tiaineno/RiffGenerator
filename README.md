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
### order###
Order will determine how many previous notes the program considers when generating the next one. Smaller number will lead to more random results. 3 is a good starting point.
### midi files###
You can use the default files when testing the program, just type metallica (this will insert every file in that folder), nevergonnagiveyouup.mid or tuikituikitahtonen.mid to insert them. You can also use your own midi-files (or folders with midi-files) by moving them in data/input. Don't forget the .mid-ending when typing single files. 
### length###
Length of the midi sequence (in notes). 16 notes is usually long enough for testing.
### starting note###
The midi value of the starting note (must be part of input). Type 40 when using metallica songs or 60 with other default midi.files.

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
