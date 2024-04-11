import sys

N = int(sys.stdin.readline())
sum = 1

for i in range(1, N+1):
    sum *= i
print(sum)