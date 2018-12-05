#############
# Common Code
#############

INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    polymer = list(f.readline().strip('\n'))

# Helper function to reduce the input list of char, output a list of char
def reduce(s):
    i = 1
    while i < len(s):
        if s[i] != s[i-1] and s[i].upper() == s[i-1].upper():
            # If two neighbors char are "aA" or "Aa", delete them
            del(s[i], s[i-1])

            # Back 1 step since we don't want to miss if the deletion created a
            # new reacting pair
            i -= 1
            continue
        i += 1
    return s

##########
# Part One
##########

print("Part One:", len(reduce(polymer)))

##########
# Part Two
##########

# Build the charset for which we want to check by removing each one
charset = set(map(lambda x: x.upper(), polymer))
results = []

for c in charset:
    # Filtered polymer doesn't contain a single occurence of char c
    filtered_polymer = list(filter(lambda x: x.upper() != c.upper(), polymer))

    l = len(reduce(filtered_polymer))

    results.append((l,c))

print("Part Two:", min(results))
