data_file = open('input.txt', 'r')
data = data_file.read().split('\n')
max_id = 0
all_ids = []
for b_pass in data:
    row = b_pass[:7]
    col = b_pass[7:]
    
    row_range = [0, 127]
    col_range = [0, 7]
    for curr_row in row:
        dist = (row_range[1] - row_range[0]) // 2
        if curr_row == 'F':
            row_range[1] -= dist + 1
        else:
            row_range[0] += dist + 1
    if row[6] == 'B':
        row_range[0] = row_range[1]
    for curr_col in col:
        dist = (col_range[1] - col_range[0]) // 2
        if curr_col == 'L':
            col_range[1] -= dist + 1
        else:
            col_range[0] += dist + 1
    if col[2] == 'R':
        col_range[0] = col_range[1]
    max_id = max(row_range[0] * 8 + col_range[0], max_id)
    all_ids.append(row_range[0] * 8 + col_range[0])

print(max_id)

all_ids.sort()
start = 6
for curr_id in all_ids:
    if curr_id != start:
        print(start)
        break
    start += 1