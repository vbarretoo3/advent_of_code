test = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

file = open('C:/Users/VictordeOliveira/Documents/GitHub/advent_of_code/2020/06/input.txt')
data = file.read()
clean_data = []
database = data
database = database.split('\n\n')
for item in database:
    clean_data.append(item.replace('\n',''))


result = []
for item in clean_data: 
    answer_count = []
    word = []
    for letter in item:
        word.append(letter)
    for letter in word:
        if letter not in answer_count:
            answer_count.append(letter)
    count = len(answer_count)
    result.append(count)

solution = 0
for item in result:
    solution += item

print(solution)
