columns = [["R", "N", "F", "V", "L", "J", "S", "M"],
           ["P", "N", "D", "Z", "F", "J", "W", "H"],
           ["W", "R", "C", "D", "G"],
           ["N", "B", "S"],
           ["M", "Z", "W", "P", "C", "B", "F", "N"],
           ["P", "R", "M", "W"],
           ["R", "T", "N", "G", "L", "S", "W"],
           ["Q", "T", "H", "F", "N", "B", "V"],
           ["L", "M", "H", "Z", "N", "F"]]

columns1 = [["Z", "N"],
            ["M", "C", "D"],
            ["P"]]

test = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

db = open("./input.txt")
data = db.read()
result = []
for line in data.splitlines():
    words = line.split()
    qty = int(words[1])
    origin = int(words[3]) - 1
    destination = int(words[5]) - 1

    # Collect items to be moved
    items_to_move = columns[origin][-qty:]

    # Remove items from origin
    columns[origin] = columns[origin][:-qty]

    # Add items to destination in reverse order
    for item in items_to_move:
        columns[destination].append(item)

for i in range(len(columns)):
    result.append(columns[i][-1])
print(result)
