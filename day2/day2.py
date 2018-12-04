#############
# Common Code
#############

INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    IDs = f.readlines()

##########
# Part One
##########

def check_double_triple(ID):
    double = 0
    triple = 0
    for letter in ID:
        count = ID.count(letter)
        if count == 2:
            double = 1
        elif count == 3:
            triple = 1

    return double, triple

d_count = 0
t_count = 0

for ID in IDs:
    has_double, has_triple = check_double_triple(ID)
    d_count += has_double
    t_count += has_triple

checksum = d_count * t_count

print("Part One:", checksum)

##########
# Part Two
##########

def hamming_distance(ID1, ID2):
    return sum([char1 != char2 for char1, char2 in zip(ID1, ID2)])

for ID1 in IDs:
    for ID2 in IDs:
        if hamming_distance(ID1, ID2) == 1:
            common_letters = [char1 for char1, char2 in zip(ID1, ID2) if char1
                    == char2]
            break;

print("Part Two:", ''.join(common_letters))
