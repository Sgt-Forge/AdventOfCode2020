data_file = open('input.txt', 'r')
data = data_file.readlines()
count = 0
for line in data:
	first_split = line.split('-')
	first = int(first_split[0]) - 1
	second_split = first_split[1].split(' ')
	second = int(second_split[0]) - 1
	letter = second_split[1][0]
	password = second_split[2]
	if password[first] == letter and password[second] != letter:
		count += 1
	if password[second] == letter and password[first] != letter:
		count += 1
print(count)
