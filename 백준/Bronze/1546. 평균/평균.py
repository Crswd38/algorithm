import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
max = 0
sum = 0

for i in range(N):
    if(a[i] > max):
        max = a[i]

for i in range(N):
    sum += a[i]/max*100

print(sum/N)