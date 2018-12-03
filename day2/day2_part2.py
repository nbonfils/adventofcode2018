def hamming_distance(ID1, ID2):
    return sum([char1 != char2 for char1, char2 in zip(ID1, ID2)])


INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    IDs = f.readlines()

for ID1 in IDs:
    for ID2 in IDs:
        if hamming_distance(ID1, ID2) == 1:
            common_letters = [char1 for char1, char2 in zip(ID1, ID2) if char1
                    == char2]
            break;

print(''.join(common_letters))
