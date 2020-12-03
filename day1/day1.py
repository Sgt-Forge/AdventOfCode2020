data_file = open('input.txt', 'r')
data = data_file.read().split('\n')
data.pop()
data = [int(x) for x in data]
print(data)

for num in data:
	remainder = 2020 - num
	if remainder in data:
		print(num * remainder)
