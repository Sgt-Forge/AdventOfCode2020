data_file = open('input.txt', 'r')
num_valid = 0
passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

data = data_file.read()
data = data.split('\n\n')
for datum in data:
    num_valid_fields = 0
    datum = datum.split('\n')
    datum = ' '.join(datum)
    for field in passport_fields:
        if field in datum:
            num_valid_fields += 1
    if num_valid_fields == 7:
        num_valid += 1

print(num_valid)

