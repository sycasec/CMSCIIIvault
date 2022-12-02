
infile = 'day1input.txt'
elves = [0]
with open(infile, 'r') as file:
    elf_count = 0
    for line in file:
        if line.rstrip() == '':
            elf_count += 1
            elves.append(0)
        else:
            elves[elf_count] += int(line.rstrip())

# print(max(elves)) - prints out max cal count elf
elves.sort(reverse=True)
print(sum(elves[:3])) 
# NOTE: part 1, elf with most calorie calcount = 71934