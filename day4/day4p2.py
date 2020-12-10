import re

data_file = open('input.txt', 'r')
num_valid = 0
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

data = data_file.read()
data = data.split('\n\n')
for datum in data:
    num_valid_fields = 0
    datum = datum.split('\n')
    datum = ' '.join(datum)
    datum = datum.split(' ')
    for field in datum:
        field = field.split(':')
        if field[0] == 'byr':
            year = int(field[1])
            if year < 1920 or year > 2002:
                break
            num_valid_fields += 1
        elif field[0] == 'iyr':
            year = int(field[1])
            if year < 2010 or year > 2020:
                break
            num_valid_fields += 1
        elif field[0] == 'eyr':
            year = int(field[1])
            if year < 2020 or year > 2030:
                break
            num_valid_fields += 1
        elif field[0] == 'hgt':
            if 'in' in field[1]:
                field[1] = field[1].replace('in', '')
                hgt = int(field[1])
                if hgt < 59 or hgt > 76:
                    break
            elif 'cm' in field[1]:
                field[1] = field[1].replace('cm', '')
                hgt = int(field[1])
                if hgt < 150 or hgt > 193:
                    break
            else:
                break
            num_valid_fields += 1
        elif field[0] == 'hcl':
            color = field[1]
            match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', field[1])
            if not match:
                break
            num_valid_fields += 1
        elif field[0] == 'ecl':
            color = field[1]
            if color not in eye_colors:
                break
            num_valid_fields += 1
        elif field[0] == 'pid':
            if len(field[1]) == 9:
                num_valid_fields += 1
            else:
                break
    if num_valid_fields == 7:
        num_valid += 1

print(num_valid)

