import sys

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

a = M[0]
b = M[1]
c = M[0]
d = M[1]

for i in range(1, N):
    M = list(map(int, sys.stdin.readline().split()))
    a = min(a, M[0])
    b = min(b, M[1])
    c = max(c, M[0])
    d = max(d, M[1])

print((d-b)*(c-a))