import sys

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = sys.stdin.readline().rstrip().split()
    print(int(A)+int(B))