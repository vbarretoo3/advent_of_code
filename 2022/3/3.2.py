test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
test2 = "RfMJcDdfdcfdddfZjdchrtZmSmCZVtqVnZmrnrtC"


def letterToNumber(letter):
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    elif 'A' <= letter <= 'Z':
        return ord(letter) - ord('A') + 27


db = open("./2022/3/input.txt")
data = db.read()
result = 0
group = []
for line in data.splitlines():
    group.append(line)
    if len(group) == 3:
        processed_letters = set()
        for a in group[0]:
            if a not in processed_letters:
                if a in group[1] and a in group[2]:
                    result += letterToNumber(a)
                    processed_letters.add(a)
        group = []

print(result)
