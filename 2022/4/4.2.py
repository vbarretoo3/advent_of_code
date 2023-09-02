test = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def calculateIds(string):
    ids = string.split("-")
    minId = int(ids[0])
    maxId = int(ids[1])
    finalIds = []
    while minId <= maxId:
        finalIds.append(minId)
        minId += 1
    return finalIds


db = open("./input.txt")
data = db.read()
result = 0

for line in data.splitlines():
    zones = line.split(",")
    zonesId1 = calculateIds(zones[0])
    zonesId2 = calculateIds(zones[1])
    sameids = []
    for id1 in zonesId1:
        for id2 in zonesId2:
            if id1 == id2:
                sameids.append(id1)
    if len(sameids) >= 1:
        result += 1

print(result)
