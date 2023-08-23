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
totalcal = []
for x in data.splitlines():
    if x != '':
        cal = cal + int(x)
    else:
        totalcal.append(cal)
        cal = 0
large = 0
for x in totalcal:
    if x > large:
        large = x
totalcal.remove(large)
large_2 = 0
for x in totalcal:
    if x > large_2:
        large_2 = x
totalcal.remove(large_2)
large_3 = 0
for x in totalcal:
    if x > large_3:
        large_3 = x
totalcal.remove(large_3)

bigtotal = large + large_2 + large_3
print(bigtotal)
