#############
# Common Code
#############

import string

#INPUT_FILE = "example.txt"
INPUT_FILE = "input.txt"

instructions = []
with open(INPUT_FILE) as f:
    for line in f:
        _, before, _, _, _, _, _, then, *_ = line.split(' ')
        instructions.append((before, then))

def init(instructions):
    # compute what are the first and last steps, all the steps left to do and the possible
    # next steps ordered alphabetically
    before_steps, then_steps = map(set, zip(*instructions))
    first_steps = before_steps - then_steps
    last_step = (then_steps - before_steps).pop()
    possible_steps = sorted(list(first_steps))
    left_steps = (before_steps & then_steps)

    # compute the requirement for each step
    steps_req = []
    for step in left_steps:
        req = (step, set([instr[0] for instr in instructions if step == instr[1]]))
        steps_req.append(req)

    steps_value = {}
    for i, letter in enumerate(string.ascii_uppercase):
        if letter in before_steps or letter in then_steps:
            steps_value[letter] = i + 1 + 60

    return steps_req, possible_steps, last_step, steps_value

##########
# Part One
##########

def part_one(instructions):
    steps_req, possible_steps, last_step, _ = init(instructions)

    steps = ''
    while len(possible_steps) > 0:
        # consume the first step that can be done
        curr_step = possible_steps.pop(0)
        steps += curr_step

        for req in steps_req:
            req[1].discard(curr_step)
            if not req[1]:
                possible_steps.append(req[0])

        # delete where set are empty in order to avoid infinite adding the same step
        steps_req = [req for req in steps_req if req[1] != set()]

        possible_steps.sort()

    return steps + last_step

print("Part One:", part_one(instructions))

##########
# Part Two
##########

def part_two(instructions):
    steps_req, possible_steps, last_step, steps_value = init(instructions)

    total_time = 0
    done_steps = []
    workers = []
    while len(done_steps) < len(steps_value) - 1:
        # find the next possible steps
        for req in steps_req:
            for done in done_steps:
                req[1].discard(done)
            if not req[1]:
                possible_steps.append(req[0])
        
        # delete where set are empty in order to avoid infinite adding the same step
        steps_req = [req for req in steps_req if req[1] != set()]

        # continue to do the steps alphabetically
        possible_steps.sort()

        # give the available steps to the workers if any idles
        new_steps = set()
        for step in possible_steps:
            if len(workers) < 5:
                workers.append((step, steps_value[step]))
                new_steps.add(step)

        # consume the steps that will be worked on
        possible_steps = [s for s in possible_steps if s not in new_steps]
        
        # steps that will be removed at the end of this iteration
        done_steps += [w[0] for w in workers if w[1] == 1]

        # each time spent is deduced from the workers
        total_time += 1
        workers = [(w[0], w[1] - 1) for w in workers if w[1] > 1]
        
    # don't forget to still do the last step
    # note: you don't have to add +1 here since the last iteration of the loop
    # will account for it
    total_time += steps_value[last_step]

    return total_time

print("Part Two:", part_two(instructions))
