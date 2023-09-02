test = """A Y
B X
C Z"""


def roundCalculation(opp, you):
    round = 0
    if you == "X":
        round += 1
    elif you == "Y":
        round += 2
    else:
        round += 3
    if opp == "A":
        if you == "X":
            round += 3
        elif you == "Y":
            round += 6
        else:
            round += 0
    elif opp == "B":
        if you == "X":
            round += 0
        elif you == "Y":
            round += 3
        else:
            round += 6
    elif opp == "C":
        if you == "X":
            round += 6
        elif you == "Y":
            round += 0
        else:
            round += 3
    return round


database = open("./2022/2/input.txt")
data = database.read()
result = 0
for x in data.splitlines():
    result = result + roundCalculation(x[0], x[2])

print(result)
