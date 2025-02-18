row = [list(map(int, input().split())) for _ in range(9)]
max_value = -1  #최댓값 -1로 초기화
row_idx, col_idx = 0,0

for i in range(9):
    for j in range(9):
        if row[i][j] > max_value:
            max_value = row[i][j]
            row_idx, col_idx = i+1, j+1
print(max_value)
print(row_idx,col_idx)