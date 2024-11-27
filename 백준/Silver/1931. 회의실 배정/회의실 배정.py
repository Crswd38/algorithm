from sys import stdin

N = int(stdin.readline())

time = [[0]*2 for _ in range(N)]

for i in range(N):
    time[i][0], time[i][1] = map(int, stdin.readline().split())
    
time.sort(key = lambda x: (x[1], x[0]))

cnt = 0
end = 0
for i, j in time:
    if i >= end:
        end = j
        cnt += 1
print(cnt)
