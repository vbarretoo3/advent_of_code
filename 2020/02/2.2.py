import pandas as pd

c = pd.read_excel("Passwords.xlsx")
df = pd.DataFrame(c)
result = []

test = {
    "Min":[1, 1, 2],
    "Max":[3, 3, 9],
    "Character": ['a', 'b', 'c'],
    "Passwords": ['abcde', 'cdefg','ccccccccc']
}

for l in range(0, len(df)):
    chars = []
    character = df['Character'][l]
    password = df['Passwords'][l]
    min = df['Min'][l]
    max = df['Max'][l]
    str = list(password)
    a = str[min-1]
    b = str[max-1]
    if character == a or character == b:
        if a != b:
            result.append(password)
print(len(result))
print(result)