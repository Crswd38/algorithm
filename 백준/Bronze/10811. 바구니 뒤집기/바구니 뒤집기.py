import sys

N, M = map(int, sys.stdin.readline().split())
balls = [0] * N
A = 0

for i in range(N):
    balls[i] = i+1

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    balls[i-1:j] = balls[i-1:j][::-1]
print(' '.join(map(str, balls)))