import sys
import math

n = int(sys.stdin.readline())
sum = 0

for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(1, arr[0]):
        for j in range(1+i, arr[0]+1):
            sum += math.gcd(arr[i],arr[j])
    print(sum)
    sum = 0