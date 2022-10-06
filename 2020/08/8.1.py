test = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''
data = open('./2020/08/input.txt')

dirty_data = data.read()
answers = dirty_data
database = answers.split('\n')
entries = []
l=0
for item in database: 
    temp = []
    temp.append(l)
    temp_entries = item.split()
    for temp_item in temp_entries:
        temp.append(temp_item)
    entries.append(temp)
    l += 1

acc = 0
item = 0
count_unique = []
c = 0
for d in range(0, len(entries)):
    if entries[c][0] not in count_unique:
        count_unique.append(entries[c][0]) 
    else:
        print(acc)
        break
    if entries[c][1] == 'acc':
        acc += int(entries[c][2])
    elif entries[c][1] == 'jmp':
        c += int(entries[c][2]) -1

    else:
        pass
    c += 1
    item += 1
