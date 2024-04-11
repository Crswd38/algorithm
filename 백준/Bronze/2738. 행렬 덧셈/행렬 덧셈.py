N, M = map(int, input().split())

matrix = []

for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        matrix[i][j] += row[j]

for i in range(N):
    print(" ".join(map(str, matrix[i])))
