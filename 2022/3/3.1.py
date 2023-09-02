test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
test2 = "RfMJcDdfdcfdddfZjdchrtZmSmCZVtqVnZmrnrtC"


def separteStrings(string):
    mid = int(len(string)/2)
    first = string[mid:]
    second = string[:mid]
    return first, second


def letterToNumber(letter):
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    elif 'A' <= letter <= 'Z':
        return ord(letter) - ord('A') + 27


def findLetter(string):
    first, second = separteStrings(string)
    for a in first:
        for b in second:
            if a == b:
                return letterToNumber(a)


db = open("./2022/3/input.txt")
data = db.read()
result = 0
for line in data.splitlines():
    result = result + findLetter(line)

print(result)
