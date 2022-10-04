test = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
file = open('C:/Users/VictordeOliveira/Documents/GitHub/advent_of_code/2020/05/input.txt')
dirty_file = file.read()
input = dirty_file.split()
result = []
database = input
for item in database:
    row = item[-3:]
    column = item[:-3]
    row_letter = list(row)
    column_letter = list(column)
    if row_letter[0] == 'R':
        if row_letter[1] == 'R':
            if row_letter[2] == 'R':
                row_value = 7
            else:
                row_value = 6
        else:
            if row_letter[2] == 'R':
                row_value = 5
            else:
                row_value = 4
    else:
        if row_letter[1] == 'R':
            if row_letter[2] == 'R':
                row_value = 3
            else:
                row_value = 2
        else:
            if row_letter[2] == 'R':
                row_value = 1
            else:
                row_value = 0
    if column_letter[0] == 'B':
        if column_letter[1] == 'B':
            if column_letter[2] == 'B':
                if column_letter[3] == 'B':
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 128
                            else:
                                column_value = 127
                        else:
                            if column_letter[6] == 'B':
                                column_value = 126
                            else:
                                column_value = 125
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 124
                            else:
                                column_value = 123
                        else:
                            if column_letter[6] == 'B':
                                column_value = 122
                            else:
                                column_value = 121
                else:
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 120
                            else:
                                column_value = 119
                        else:
                            if column_letter[6] == 'B':
                                column_value = 118
                            else:
                                column_value = 117
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 116
                            else:
                                column_value = 115
                        else:
                            if column_letter[6] == 'B':
                                column_value = 114
                            else:
                                column_value = 113
            else:
                if column_letter[3] == '':
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 112
                            else:
                                column_value = 111
                        else:
                            if column_letter[6] == 'B':
                                column_value = 110
                            else:
                                column_value = 109
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 108
                            else:
                                column_value = 107
                        else:
                            if column_letter[6] == 'B':
                                column_value = 106
                            else:
                                column_value = 105
                else:
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 104
                            else:
                                column_value = 103
                        else:
                            if column_letter[6] == 'B':
                                column_value = 102
                            else:
                                column_value = 101
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 100
                            else:
                                column_value = 99
                        else:
                            if column_letter[6] == 'B':
                                column_value = 98
                            else:
                                column_value = 97
        else:
            if column_letter[2] == 'B':
                if column_letter[3] == 'B':
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 96
                            else:
                                column_value = 95
                        else:
                            if column_letter[6] == 'B':
                                column_value = 94
                            else:
                                column_value = 93
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 92
                            else:
                                column_value = 91
                        else:
                            if column_letter[6] == 'B':
                                column_value = 90
                            else:
                                column_value = 89
                else:
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 88
                            else:
                                column_value = 87
                        else:
                            if column_letter[6] == 'B':
                                column_value = 86
                            else:
                                column_value = 85
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 84
                            else:
                                column_value = 83
                        else:
                            if column_letter[6] == 'B':
                                column_value = 82
                            else:
                                column_value = 81
            else:
                if column_letter[3] == 'B':
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 80
                            else:
                                column_value = 79
                        else:
                            if column_letter[6] == 'B':
                                column_value = 78
                            else:
                                column_value = 77
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 76
                            else:
                                column_value = 75
                        else:
                            if column_letter[6] == 'B':
                                column_value = 74
                            else:
                                column_value = 73
                else:
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 72
                            else:
                                column_value = 71
                        else:
                            if column_letter[6] == 'B':
                                column_value = 70
                            else:
                                column_value = 69
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 68
                            else:
                                column_value = 67
                        else:
                            if column_letter[6] == 'B':
                                column_value = 66
                            else:
                                column_value = 65
    else:
        if column_letter[1] == 'B':
            if column_letter[2] == 'B':
                if column_letter[3] == 'B':
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 64
                            else:
                                column_value = 63
                        else:
                            if column_letter[6] == 'B':
                                column_value = 62
                            else:
                                column_value = 61
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 60
                            else:
                                column_value = 59
                        else:
                            if column_letter[6] == 'B':
                                column_value = 58
                            else:
                                column_value = 57
                else:
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 56
                            else:
                                column_value = 55
                        else:
                            if column_letter[6] == 'B':
                                column_value = 54
                            else:
                                column_value = 53
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 52
                            else:
                                column_value = 51
                        else:
                            if column_letter[6] == 'B':
                                column_value = 50
                            else:
                                column_value = 49
            else:
                if column_letter[3] == 'B':
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 48
                            else:
                                column_value = 47
                        else:
                            if column_letter[6] == 'B':
                                column_value = 46
                            else:
                                column_value = 45
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 44
                            else:
                                column_value = 43
                        else:
                            if column_letter[6] == 'B':
                                column_value = 42
                            else:
                                column_value = 41
                else:
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 40
                            else:
                                column_value = 39
                        else:
                            if column_letter[6] == 'B':
                                column_value = 38
                            else:
                                column_value = 37
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 36
                            else:
                                column_value = 35
                        else:
                            if column_letter[6] == 'B':
                                column_value = 34
                            else:
                                column_value = 33
        else:
            if column_letter[2] == 'B':
                if column_letter[3] == 'B':
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 32
                            else:
                                column_value = 31
                        else:
                            if column_letter[6] == 'B':
                                column_value = 30
                            else:
                                column_value = 29
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 28
                            else:
                                column_value = 27
                        else:
                            if column_letter[6] == 'B':
                                column_value = 26
                            else:
                                column_value = 25
                else:
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 24
                            else:
                                column_value = 23
                        else:
                            if column_letter[6] == 'B':
                                column_value = 22
                            else:
                                column_value = 21
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 20
                            else:
                                column_value = 19
                        else:
                            if column_letter[6] == 'B':
                                column_value = 18
                            else:
                                column_value = 17
            else:
                if column_letter[3] == 'B':
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 16
                            else:
                                column_value = 15
                        else:
                            if column_letter[6] == 'B':
                                column_value = 14
                            else:
                                column_value = 13
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 12
                            else:
                                column_value = 11
                        else:
                            if column_letter[6] == 'B':
                                column_value = 10
                            else:
                                column_value = 9
                else:
                    if column_letter[4] == 'B':
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 8
                            else:
                                column_value = 7
                        else:
                            if column_letter[6] == 'B':
                                column_value = 6
                            else:
                                column_value = 5
                    else:
                        if column_letter[5] == 'B':
                            if column_letter[6] == 'B':
                                column_value = 4
                            else:
                                column_value = 3
                        else:
                            if column_letter[6] == 'B':
                                column_value = 2
                            else:
                                column_value = 1
    column_value = column_value-1
    id = column_value * 8 + row_value
    result.append(id)

solution = result[0]
for ids in result:
    if ids > solution:
        solution = ids

print(solution)
