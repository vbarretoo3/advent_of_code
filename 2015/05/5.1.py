vowels = ['a','e','i','o','u']
naughty = ['ab', 'cd', 'pq', 'xy']
test = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
file = open('./2015/05/input.txt').read().splitlines()

data = file
nice = []

for item in data:
    naughty_valid = False
    double_letters = False
    vowel_count = 0
    for letter in item:
        if letter in vowels:
            vowel_count += 1
    l = len(item)
    for c in range(0, l-1):
        if item[c] == item[c+1]:
            double_letters = True
    for code in naughty:
        if code in item:
            naughty_valid = True
    if vowel_count >= 3 and double_letters == True and naughty_valid == False:
        nice.append(item)
print(len(nice))