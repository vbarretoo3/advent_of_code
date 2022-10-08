test = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
file = open('./2015/05/input.txt').read().splitlines()

data = file
nice = []

for item in data:
    term_1 = False
    term_2 = False
    c = len(item)
    if c > 4:
        for i in range(0, c-2):
            if item[i] == item[i+2] and item[i] != item[i+1]:
                term_1 = True
        for i in range(0, c-2):
            double = item[i] + item[i+1]
            if item.count(double) >= 2:
                term_2 = True
        if term_1 == True and term_2 == True:
            nice.append(nice)
print(nice)
print(len(nice))