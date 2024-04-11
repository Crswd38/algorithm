import sys
import math

N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
data = []
result = 0

for i in range(N):
    data.append(abs(S - A[i]))

for i in data:
    result = math.gcd(result, i)

print(result)