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


INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    IDs = f.readlines()

d_count = 0
t_count = 0

for ID in IDs:
    has_double, has_triple = check_double_triple(ID)
    d_count += has_double
    t_count += has_triple

checksum = d_count * t_count

print(checksum)

