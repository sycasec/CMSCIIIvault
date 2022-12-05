#! usr/bin/python3

with open("day4in.txt", 'r') as file:
    contains_count = 0
    for line in file:
        first, second = line.rstrip().split(',')
        first = first.split('-')
        second = second.split('-')
        first = [int(x) for x in first if x.isdigit()]
        second = [int(x) for x in second if x.isdigit()]
        # if (first[0] <= second[0] and first[1] >= second[1]) or (second[0] <= first[0] and second[1] >= first[1]):

        if first[0] <= second[0] <= first[1] or second[0] <= first[0] <= second[1] or first[0] <= second[1] <= first[1] or second[0] <= first[1] <= second[1]:
            contains_count += 1



    print(contains_count) 
