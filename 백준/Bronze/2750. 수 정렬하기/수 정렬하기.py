import sys

N = int(sys.stdin.readline().strip())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()
for i in arr:
    print(i)