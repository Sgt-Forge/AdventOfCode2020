data_file = open('input.txt', 'r')
data = []
while(True):
    newline = data_file.readline()
    if newline == '':
        break
    data.append(newline.rstrip())
    
x_pos, x_max = 0, len(data[0])
y_pos, y_max = 0, len(data)
trees = 0

while y_pos < y_max:
    if data[y_pos][x_pos] == '#':
        trees += 1

    x_pos += 1
    x_pos %= x_max
    y_pos += 2

print(trees)