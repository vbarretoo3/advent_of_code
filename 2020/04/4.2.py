from sys import int_info


def convert_to_dictionary(passport_list):
    dictionary = {}

    for item in passport_list:
        records = item.split(":")
        key = records[0]
        value = records[1]
        dictionary[key] = value
    return dictionary

def is_valid_passport(passport):
    has_birth_year = "byr" in passport
    has_issue_year = "iyr" in passport
    has_expiration_year = "eyr" in passport
    has_height = "hgt" in passport
    has_hair_color = "hcl" in passport
    has_eye_color = "ecl" in passport
    has_passport_id = "pid" in passport
    has_country_id = "cid" in passport
    
    return (
        has_birth_year and
        has_issue_year and
        has_expiration_year and
        has_height and
        has_hair_color and
        has_eye_color and
        has_passport_id
    )
def validade_passports(passport_to_be_validated):
    valid_birth_year = 1920 <= int(passport_to_be_validated["byr"]) <=2002
    valid_issue_year = 2010 <= int(passport_to_be_validated["iyr"]) <= 2020
    valid_expiration_year = 2020 <= int(passport_to_be_validated["eyr"]) <= 2030

    valid_height = False
    height_units = passport_to_be_validated['hgt'][-2:]
    if height_units == 'cm':
        height = int(passport_to_be_validated['hgt'][:-2])
        valid_height = 150 <= height <= 193
    elif height_units == 'in':
        height = int(passport_to_be_validated['hgt'][:-2])
        valid_height = 59 <= height <= 76
    
    def valid_hex(string):
        test_value = string.lower()
        is_valid = True

        for character in string:
            if character not in "0123456789abcdef":
                is_valid = False
                break
        return is_valid

    valid_hair_color = False
    if len(passport_to_be_validated['hcl']) == 7:
        digits = passport_to_be_validated['hcl'][1:]
        valid_hair_color = valid_hex(digits)
    valid_eye_color = passport_to_be_validated['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
    def valid_passport(value):
        is_valid = False

        if len(value) == 9:
            is_valid = True

            for character in value:
                if character not in "0123456789":
                    is_valid = False
                    break

        return is_valid
    
    valid_passport_id = valid_passport(passport_to_be_validated['pid'])
    
    return(
        valid_birth_year and
        valid_issue_year and
        valid_expiration_year and
        valid_height and
        valid_hair_color and
        valid_eye_color and
        valid_passport_id
    )



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

database = input
passports = []
for item in database:
    passports.append(convert_to_dictionary(item))

valid_passports = [passport for passport in passports if is_valid_passport(passport)]


truly_valid_passports = [passport for passport in valid_passports if validade_passports(passport)]
print(len(truly_valid_passports))