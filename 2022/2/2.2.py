test = """A Y
B X
C Z"""


def roundCalculation(opp, you):
    round = 0
    if opp == "A":
        if you == "X":
            round += 3
        elif you == "Y":
            round += 4
        else:
            round += 8
    elif opp == "B":
        if you == "X":
            round += 1
        elif you == "Y":
            round += 5
        else:
            round += 9
    elif opp == "C":
        if you == "X":
            round += 2
        elif you == "Y":
            round += 6
        else:
            round += 7
    return round


database = open("./2022/2/input.txt")
data = database.read()
result = 0
for x in data.splitlines():
    result = result + roundCalculation(x[0], x[2])

print(result)
