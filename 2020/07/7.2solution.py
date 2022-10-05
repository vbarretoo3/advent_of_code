from collections import defaultdict


f = open('C:/Users/VictordeOliveira/Documents/GitHub/advent_of_code/2020/07/input.txt')
rules = f.readlines()

bags = defaultdict(dict)

for rule in rules:
    parts = rule.split(" ")
    color = " ".join(parts[:2])
    in_parts = " ".join(parts[4:]).split(",")
    for part in in_parts:
        if not "no other bags" in part:
            sp = part.strip().split(" ")
            bags[color][" ".join(sp[1:3])] = int(sp[0])
        else:
            bags[color] = {}


def can_hold(in_color, out_color):
    if in_color in str(bags[out_color]):
        return True
    return any([can_hold(in_color, b) for b in bags[out_color]])


def num_inside(color):
    return sum([bags[color][b] * (1 + num_inside(b)) for b in bags[color]])


part1 = sum([can_hold("shiny gold", bag) for bag in bags])
print(f"Part 1: {part1}")
print(f'Part 2: {num_inside("shiny gold")}')