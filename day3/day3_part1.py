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

overlap_grid = [0] * 1000 * 1000

# Fill the grid according to the claim
for claim in claims:
    for x in range(claim[1], claim[1] + claim[3]):
        for y in range(claim[2], claim[2] + claim[4]):
            overlap_grid[x + 1000 * y] += 1

# > 2 means 2 or more have claimed this inch
print(sum(x >= 2 for x in overlap_grid))
