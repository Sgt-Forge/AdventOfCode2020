data_file = open('input.txt', 'r')
data = data_file.read().split('\n')
data.pop()

data = [int(x) for x in data]
data.sort()
start = 0
while start < len(data) - 2:
	i, j = start + 1, len(data) - 1
	while i < j:
		curr_sum = data[start] + data[i] + data[j]
		if curr_sum > 2020:
			j -= 1
		elif curr_sum < 2020:
			i += 1
		else:
			print('Answer: ', data[start] * data[i] * data[j])
			exit(0)
	start += 1
print('No answer found!')

