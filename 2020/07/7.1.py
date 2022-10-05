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

def check_color(entry):
    color_unique = []
    for item in dirty:
        if entry in item:
            word = item.split()
            color_1 = word[0] + ' ' + word[1]
            if color_1 != entry:
                if color_1 not in color_unique:
                    color_unique.append(color_1)
    for item in color_unique:
        if item not in color_unique_total:
            color_unique_total.append(item)                    
    for item in color_unique:
        check_color(item)
    
    return len(color_unique_total)


solution = check_color('shiny gold')
    

print(solution)