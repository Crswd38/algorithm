
matrix = []
max_value = -1
a=0
b=0

for i in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(9):
    for j in range(9):
        if max_value < matrix[i][j]:
            max_value = matrix[i][j]
            a = i + 1
            b = j + 1
            
print(max_value)
print(a, b)

