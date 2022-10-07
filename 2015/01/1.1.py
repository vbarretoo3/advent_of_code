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

for item in database:
    pos = item.count('(')
    neg = item.count(')')
    count = pos - neg
    print(count)
