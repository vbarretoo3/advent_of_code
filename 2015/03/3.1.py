from traceback import print_exc


test = ['>', '^>v<', '^v^v^v^v^v']
file = open('./2015/03/input.txt').read()
database = file

values = [[0, 0]]
H = 0
V = 0
c = 0
for item in database:
    cordinates = []
    if item == '>':
        V += 1
    elif item == '<':
        V -= 1
    elif item == 'v':
        H -= 1
    else:
        H += 1
    cordinates.append(V)
    cordinates.append(H)
    if cordinates not in values:
        values.append(cordinates)
print(len(values))

