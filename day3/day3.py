data_file = open('input.txt', 'r')
data = []
while(True):
    newline = data_file.readline()
    if newline == '':
        break
    data.append(newline)
    
x_pos, x_max = 0, len(data)
y_pos = 0


