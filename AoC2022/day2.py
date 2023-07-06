# 1 A, X : ROCK 
# 2 B, Y : PAPER 
# 3 C, Z : SCISSORS
# 0L 3D 6W

with open('day2input.txt', 'r') as file:
    total_s = 0
    for line in file:
        elf, me = line.rstrip().split()

        if elf == 'A': # ROCK
            if me == 'X': # LOSE
                total_s += 3
            elif me == 'Y': # DRAW 
                total_s += 4
            elif me == 'Z': # WiN
                total_s += 8
        elif elf == 'B': # PAPER
            if me == 'X':
                total_s += 1
            elif me == 'Y':
                total_s += 5
            elif me == 'Z':
                total_s += 9
        elif elf == 'C': # SCISSORS
            if me == 'X':
                total_s += 2
            elif me == 'Y':
                total_s += 6
            elif me == 'Z':
                total_s += 7

print(total_s)
        
