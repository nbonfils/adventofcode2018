#############
# Common Code
#############

#INPUT_FILE = "example.txt"
INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    license = list(map(int, f.readline().split(' ')))

##########
# Part One
##########

def part_one(license, pos):
    # get number of childs and number of metadata
    num_child = license[pos]
    num_metadata = license[pos + 1]

    # if there is no child return the metadata array and the size of the node in
    # the license number array
    if num_child == 0:
        return license[pos + 2:pos + 2 + num_metadata], 2 + num_metadata
    else:
        # get the first child metadata + size
        metadata, total_size = part_one(license, pos + 2)

        # build a metadata array containing all metadata of the child nodes
        child_metadata = []
        child_metadata += metadata
        for i in range(num_child - 1):
            metadata, size = part_one(license, pos + 2 + total_size)
            child_metadata += metadata
            total_size += size

        # find the position of the current node metadata
        metadata_idx = pos + 2 + total_size
        metadata = license[metadata_idx:metadata_idx + num_metadata]

        return child_metadata + metadata, total_size + 2 + num_metadata

metadatas, size = part_one(license, 0)

print("Part One:", sum(metadatas))

##########
# Part Two
##########

def part_two(license, pos):
    # get number of childs and number of metadata
    num_child = license[pos]
    num_metadata = license[pos + 1]

    # if there is no child return the metadata array and the size of the node in
    # the license number array
    if num_child == 0:
        return license[pos + 2:pos + 2 + num_metadata], 2 + num_metadata
    else:
        # get the first child metadata + size
        metadata, total_size = part_two(license, pos + 2)

        # build a metadata array containing ARRAY of metadata FROM the child nodes
        # notice the "append" instead of "+="
        child_metadata = []
        child_metadata.append(metadata)
        for i in range(num_child - 1):
            metadata, size = part_two(license, pos + 2 + total_size)
            child_metadata.append(metadata)
            total_size += size

        # find the position of the current node metadata
        metadata_idx = pos + 2 + total_size
        metadata = license[metadata_idx:metadata_idx + num_metadata]

        # build the resulting metadata according to the index in the metadata
        resulting_metadata = []
        for m in metadata:
            if 0 < m and m <= len(child_metadata):
                resulting_metadata += child_metadata[m - 1]

        return resulting_metadata, total_size + 2 + num_metadata

metadatas, size = part_two(license, 0)

print("Part Two:", sum(metadatas))
