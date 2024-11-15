import sys

N = int(sys.stdin.readline())
A = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
B = sys.stdin.readline().split()

for i in B:
    print(1 if i in A else 0)