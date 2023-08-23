test = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

'''
database = open("./2022/1/input.txt")
data = database.read()
cal = 0
totalcal = 0
for x in data.splitlines():
    if x != '':
        cal = cal + int(x)
    else:
        if cal > totalcal:
            totalcal = cal
        cal = 0
print(totalcal)
