
N = int(input())
paper = [[False]*100 for _ in range(100)]
sum = 0

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(10):
        for j in range(10):
            paper[a+i][b+j] = True

for i in range(100):
    for j in range(100):
        if paper[i][j]:
            sum += 1
print(sum)