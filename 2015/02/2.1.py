test = [[2,3,4], [1, 1, 10]]
file = open('2015/02/input.txt').read().splitlines()
data = []
for i in file:
    items = sorted(map(int, i.split('x')))
    values = []
    if items != '':
        for item in items:
            values.append(item)
        data.append(values)

database = data
result = 0
for i in database:
    if len(i) < 3:
        pass
    else:
        l = int(i[0])
        w = int(i[1])
        h = int(i[2])
        area = 2*l*w + 2*w*h + 2*h*l
        addition = l*w
        result += area + addition

print(result)
