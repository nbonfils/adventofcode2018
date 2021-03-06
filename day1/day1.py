#############
# Common Code
#############

INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    freq_change = [int(line) for line in f]

##########
# Part One
##########

print("Part One:", sum(freq_change))

##########
# Part Two
##########

seen_freq = set()
curr_freq = 0
i = 0
while curr_freq not in seen_freq:
    seen_freq.add(curr_freq)
    curr_freq = curr_freq + freq_change[i]
    i = (i + 1) % len(freq_change)

print("Part Two:", curr_freq)
