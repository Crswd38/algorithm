import sys

N, M = map(int, sys.stdin.readline().split())
balls = [0] * N

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for b in range(i-1, j):
        balls[b] = k

print(' '.join(map(str, balls)))