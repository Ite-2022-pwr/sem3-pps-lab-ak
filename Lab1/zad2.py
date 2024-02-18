#!/usr/bin/env python3

# Program wczytujący plik.txt i liczący indywidualne wystąpienia znaków

FILE = 'plik.txt'

characters = {}

try:
    with open(FILE, "r") as fh:
        for line in fh:
            for char in line:
                #if char.isalnum():
                characters.setdefault(char, 0)
                characters[char] += 1
except OSError as e:
    print(e)
else:
    print(characters)
