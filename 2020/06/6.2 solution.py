import string
import sys


with open('C:/Users/VictordeOliveira/Documents/GitHub/advent_of_code/2020/06/input.txt') as f:
    answers = f.read().strip().split("\n\n")

part1 = sum([len(set(ans.replace("\n", ""))) for ans in answers])
print(f"Part 1: {part1}")


count = 0
for ans in answers:
    ind_ans = ans.split("\n")
    for c in string.ascii_lowercase:
        count += all([c in a for a in ind_ans])

print(f"Part 2: {count}")