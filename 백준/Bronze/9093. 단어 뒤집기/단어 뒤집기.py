import sys

T = int(sys.stdin.readline())

for i in range(T):
    A = sys.stdin.readline().split()
    for j in A:
        print(j[::-1], end=' ')