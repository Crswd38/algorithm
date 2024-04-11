import sys

N, M = map(int, sys.stdin.readline().split())
balls = [0] * N
A = 0

for i in range(N):
    balls[i] = i+1

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    k = balls[i-1]
    balls[i-1] = balls[j-1]
    balls[j-1] = k
print(' '.join(map(str, balls)))
