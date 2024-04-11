import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
minimum = 1000000
maximum = -1000000

for i in range(N):
    if(minimum > A[i]):
        minimum = A[i]
    if(maximum < A[i]):
        maximum = A[i]   
print(f"{minimum} {maximum}")