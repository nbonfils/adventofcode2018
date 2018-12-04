#############
# Common Code
#############

INPUT_FILE = "input.txt"

# Read the input in order to build a list of claims
with open(INPUT_FILE) as f:
    claims = []
    for line in f:
        # Parse a claim string in order to extract the values
        # Example claim string: #123 @ 3,2: 5x4
        split = line.split(' ')
        ID = split[0]
        left, top = list(map(int, split[2].replace(':', '').split(',')))
        width, height = list(map(int, split[3].split('x')))

        # A claim looks like this
        claim = [
                ID,     # 0
                left,   # 1
                top,    # 2
                width,  # 3
                height, # 4
                ]
        
        # Add the claim to the list of claims
        claims.append(claim)

##########
# Part One
##########

overlap_grid = [0] * 1000 * 1000

# Fill the grid according to the claim
for claim in claims:
    for x in range(claim[1], claim[1] + claim[3]):
        for y in range(claim[2], claim[2] + claim[4]):
            overlap_grid[x + 1000 * y] += 1

# > 2 means 2 or more have claimed this inch
print("Part One:", sum(x >= 2 for x in overlap_grid))

##########
# Part Two
##########

# Helper function that returns True if overlap happens
def overlap(claim1, claim2):
    if claim1[1] < claim2[1]:
        # claim1 is left of claim2
        horizontal_overlap = min((claim1[1] + claim1[3]) - claim2[1], claim2[3])
    else:
        # claim1 is rigth or same width of claim2
        horizontal_overlap = min((claim2[1] + claim2[3]) - claim1[1], claim1[3])

    if claim1[2] < claim2[2]:
        # claim1 is above claim2
        vertical_overlap = min((claim1[2] + claim1[4]) - claim2[2], claim2[4])
    else:
        # claim1 is below or same height of claim2
        vertical_overlap = min((claim2[2] + claim2[4]) - claim1[2], claim1[4])

    if horizontal_overlap > 0 and vertical_overlap > 0:
        # Overlap happens !
        return True

    return False

# Simply break when there is no overlaping claims
for claim1 in claims:
    claim_id = claim1[0]
    for claim2 in [claim for claim in claims if claim[0] != claim1[0]]:
        if overlap(claim1, claim2):
            break
    else:
        break

print("Part Two:", claim_id)
