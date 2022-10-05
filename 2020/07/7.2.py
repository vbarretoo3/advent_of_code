from turtle import color
from numpy import append


test = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''
data =  open('C:/Users/VictordeOliveira/Documents/GitHub/advent_of_code/2020/07/input.txt')
input = data.read()
database = input
answers = database.strip()
dirty = answers.split('\n')
colors_line = []
color_unique_total = []
bags = []
volume_number = []
original = []
def check_color(entry):
    color_1 = ''
    color_2 = ''
    color_3 = ''
    quantity = 0
    quantity_2 = 0
    volume = 0
    color_unique = []
    for item in dirty:
        if entry in item:
            word = item.split()
            color_1 = word[0] + ' ' + word[1]
            if color_1 == entry:
                color_2 = word[5] + ' ' + word[6]
                volume =0
                if color_2 != 'other bags.':
                    quantity = int(word[4])
                    color_unique.append(color_2)
                    volume = 1
                    try:
                        color_3 = word[9] + ' ' + word[10]
                        quantity_2 = int(word[8])
                        color_unique.append(color_3)
                        volume = 2
                        try:
                            color_4 = word[13] + ' ' + word[14]
                            quantity_3 = int(word[12])
                            color_unique.append(color_4)
                            volume = 3
                            try:
                                color_5 = word[17] + ' ' + word[18]
                                quantity_4 = int(word[16])
                                color_unique.append(color_5)
                                volume = 4
                            except:
                                pass
                        except:
                            pass
                    except:
                        pass
                    volume_number.append(volume)
                    original.append(color_1)
                    bags.append(quantity)
                    color_unique_total.append(color_2)
                    if volume >= 2:
                        bags.append(quantity_2)
                        color_unique_total.append(color_3)    
                        if volume >= 3:
                            bags.append(quantity_3)
                            color_unique_total.append(color_4)
                            if volume >= 4:
                                bags.append(quantity_4)
                                color_unique_total.append(color_5)                 
    for item in color_unique:
        check_color(item)
    
    return (bags, volume_number, original, color_unique_total)


solution = check_color('shiny gold')

variety = solution[0]
delimiter = solution[1]
original_color = solution[2]
secundary_color = solution[3]

print(f'''
    {variety}\n
    {delimiter}\n
    {original_color}\n
    {secundary_color}
''')
n=0
for c in original_color:
    sn = 0
    for a in range(0, n):
        sn = sn + delimiter[a]
    try:
        if secundary_color[sn] != original_color[n+1]:
            test_2 = 0
            for a in range(0, delimiter[n]):
                test_2 = variety[sn+a] + test_2
            test_2 = test_2*variety[sn]
    except:
        pass
    try:
        print(test_2)
    except:
        pass
    n = n+1
