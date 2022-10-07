test='''(())
()()
(((
(()(()(
))(((((
())
))(
)))'''
file = open('./2015/01/input.txt')
answers = file.read()
data = answers
database = data.split('\n')
item_count = 0

for item in database:
    count = 0
    for i in item:
        if i =="(":
            count += 1
        else:
            count -= 1
        item_count += 1
        if count == -1:
            print(item_count)
            break
    print(count)
