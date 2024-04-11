import sys

arr = []
S = sys.stdin.readline().strip()
length = len(S)
for i in range(length):
    arr.append(S[i:length])
arr.sort()

for i in arr:
    print(i)