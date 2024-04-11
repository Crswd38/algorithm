import sys

N = int(sys.stdin.readline())
sum = 1
count = 0

for i in range(1, N+1):
    sum *= i

for i in range(len(str(sum))-1, 0, -1):
    if str(sum)[i] == "0":
        count += 1
    else:
        break

print(count)