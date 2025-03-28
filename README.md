# Riff Generator

The Riff Generator is a Python program that creates random midi sequences based on midi files used as an input. The program uses Markov chain to generate the riffs. The program will print the outcome and save the result as an midi file in /data/output.

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
**order**
Order will determine how many previous notes the program considers when generating the next one. Smaller number will lead to more random results. 3 is a good starting point.
**midi files**
Every midi file you want to use as an input must be located in data/input/. You can also insert a directory which contains midi files. Don't forget the .mid-ending when inserting single files.
**length**
length of the midi sequence (in notes)
**starting note**
the starting note (must be part of input)

## Tests and coverage ##
run tests:
```bash
poetry run pytest .
```

run coverage and view the report:
```bash
poetry run coverage run -m pytest
poetry run coverage html
```
