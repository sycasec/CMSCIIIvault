#! usr/bin/python3

stacks = []
stacks.append([c for c in "NBDTVGZJ"])
stacks.append([c for c in "SRMDWPF"])
stacks.append([c for c in "VCRSZ"])
stacks.append([c for c in "RTJZPHG"])
stacks.append([c for c in "TCJNDZQF"])
stacks.append([c for c in "NVPWGSFM"])
stacks.append([c for c in "GCVBPQ"])
stacks.append([c for c in "ZBPN"])
stacks.append([c for c in "WPJ"])

# this wasnt as much of a pain thanks to vim motions

def print_stacks():
    for i in range(len(max(stacks, key=len)), -1, -1):
        to_print = []
        for stack in stacks:
            try:
                to_print.append(stack[i])
            except IndexError:
                to_print.append(' ')

        print(to_print)


def move_crates(amt: int, src: int, dest: int):
    crane = stacks[src-1][-amt:]
    # crane.reverse() for part 1, leave as is for part 2
    stacks[src-1] = stacks[src-1][:-amt] 
    stacks[dest-1].extend(crane)

with open("day5in.txt", 'r') as file:
    for line in file:
        amt, src, dest = [int(c) for c in line.rstrip().split() if c.isdigit()]
        move_crates(amt, src, dest)
        

topcrates = []
for stack in stacks:
    topcrates.append(stack.pop())

print(''.join(topcrates))

