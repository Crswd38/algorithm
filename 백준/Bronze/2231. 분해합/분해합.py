import sys

n = int(sys.stdin.readline())
result = 0
sum = 0
for i in range(1, n+1):
    for j in str(i):
        sum += int(j)
    if i + sum == n:
        result = i
        break
    sum = 0
print(result)
