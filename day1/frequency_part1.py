import os

INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    resulting_freq = sum([int(line) for line in f])

print(resulting_freq)
