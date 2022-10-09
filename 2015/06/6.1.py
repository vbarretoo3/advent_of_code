def on(x, y):
    cordinate_1 = x.split(',')
    cordinate_2 = y.split(',')
    x_dif = int(cordinate_2[0]) - int(cordinate_1[0]) +1
    y_dif = int(cordinate_2[1]) - int(cordinate_1[1]) +1
    for r in range(0, x_dif):
        for l in range (0, y_dif):
            for item in lights:
                if item['horizontal'] == r + int(cordinate_1[0]) and item['vertical'] == l + int(cordinate_1[1]):
                    item['power'] = 1
    return

def off(x, y):
    cordinate_1 = x.split(',')
    cordinate_2 = y.split(',')
    x_dif = int(cordinate_2[0]) - int(cordinate_1[0]) +1
    y_dif = int(cordinate_2[1]) - int(cordinate_1[1]) +1
    for r in range(0, x_dif):
        for l in range (0, y_dif):
            for item in lights:
                if item['horizontal'] == r + int(cordinate_1[0]) and item['vertical'] == l + int(cordinate_1[1]):
                    item['power'] = 0
    return

def toogle(x, y):
    cordinate_1 = x.split(',')
    cordinate_2 = y.split(',')
    x_dif = int(cordinate_2[0]) - int(cordinate_1[0]) +1
    y_dif = int(cordinate_2[1]) - int(cordinate_1[1]) +1
    for r in range(0, x_dif):
        for l in range (0, y_dif):
            for item in lights:
                if item['horizontal'] == r + int(cordinate_1[0]) and item['vertical'] == l + int(cordinate_1[1]):
                    if item['power'] == 0:
                        item['power'] = 1
                    else:
                        item['power'] = 0
    return

lights = []
file = open('./2015/06/input.txt').read().splitlines()
comands = []

for i in range(0, 1000):
    for c in range(0, 1000):
        light = {
            'horizontal': i,
            'vertical': c,
            'power': 0
        }
        lights.append(light)

for i in file:
    print(file.index(i))
    temp = i.split()
    if len(temp) == 4:
        temp_command = toogle(temp[1], temp[3])
    else:
        if temp[1] == 'on':
            temp_command = on(temp[2], temp[4])
        else:
            temp_command = off(temp[2], temp[4])

count = 0

for i in lights:
    if i['power'] == 1:
        count += 1

print(count)