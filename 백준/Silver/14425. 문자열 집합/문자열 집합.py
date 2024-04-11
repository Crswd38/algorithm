import sys

N, M= map(int, sys.stdin.readline().split())
S = set()
sum = 0
A = []

for _ in range(N):
    S.add(sys.stdin.readline().strip())

for _ in range(M):
    A = sys.stdin.readline().strip()
    if A in S:
        sum += 1

print(sum)