test = ['>', '^>v<', '^v^v^v^v^v']
file = open('./2015/03/input.txt').read()
database = file

values = [[0, 0]]
H = 0
V = 0
c = 0
santa = []
r_santa = []
for item in database:
    for i in item:
        if c % 2 == 0:
            santa.append(i)
        else:
            r_santa.append(i)
        c = c + 1
data =[santa, r_santa]
for i in data:
    H = 0
    V = 0
    for c in i:
        for item in c:
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
