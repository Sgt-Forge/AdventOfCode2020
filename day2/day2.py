data_file = open('input.txt', 'r')
data = data_file.readlines()
count = 0
for line in data:
	first_split = line.split('-')
	min = int(first_split[0])
	second_split = first_split[1].split(' ')
	max = int(second_split[0])
	letter = second_split[1][0]
	print(min, max, letter)
	password = second_split[2]
	letter_count = password.count(letter)
	if letter_count >= min and letter_count <= max:
		count += 1
print(count)
