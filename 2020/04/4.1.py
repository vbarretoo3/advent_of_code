test = [['ecl:gry', 'pid:860033327', 'eyr:2020', 'hcl:#fffffd', 'byr:1937', 'iyr:2017', 'cid:147', ' hgt:183cm'], ['iyr:2013', ' ecl:amb', ' cid:350', ' eyr:2023', ' pid:028048884', ' hcl:#cfa07d', ' byr:1929'], ['hcl:#ae17e1', ' iyr:2013', ' eyr:2024', ' ecl:brn', ' pid:760753108', ' byr:1931', ' hgt:179cm'], ['hcl:#cfa07d', ' eyr:2025', ' pid:166559648', ' iyr:2011', ' ecl:brn', ' hgt:59in']]
file = open('C:/Users/VictordeOliveira/Documents/GitHub/advent_of_code/2020/04/input.txt')
dirty_file = file.read()
separated_entries = dirty_file.split('\n\n')
clean_data = []
for item in separated_entries:
    clean_data.append(item.replace('\n', " "))

input = []

for item in clean_data:
    input.append(item.split())

passports = 0

database = input

for item in database:
    if len(item)>= 7:
        if len(item) == 7:
            valid = 0
            for fields in item:
                if fields.strip().startswith('cid') == True:
                    valid += 1
            if valid == 0:
                passports += 1
        elif len(item) == 8:
            passports += 1
print(passports)
