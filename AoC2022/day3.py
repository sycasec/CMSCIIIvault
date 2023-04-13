import string
from collections import Counter

charlist = [c for c in string.ascii_letters]

def part1():
    with open("day3input.txt", "r") as file:
        priority_sum = 0
        for line in file:
            half_len = int(len(line.rstrip())/2)
            first,second = line[:half_len], line[half_len:].rstrip() 
            count1 = Counter(first)
            count2 = Counter(second)
            commonChar = list((count1 & count2).elements())[0]

            priority_sum += charlist.index(commonChar) + 1

    print(priority_sum)


with open("day3input.txt", 'r') as file:
    line_count = 0
    gang = []
    priority_sum = 0
    for line in file:
        gang.append(Counter(line.rstrip()))
        line_count += 1

        if line_count == 3:
            commonChar = list(((gang[0] & gang[1]) & gang[2]).elements())[0]
            priority_sum += (charlist.index(commonChar) + 1)


            gang.clear()
            line_count = 0
    
    print(priority_sum)
        

