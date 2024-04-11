import sys

N = int(sys.stdin.readline().strip())
list1 = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
list2 = list(map(int, sys.stdin.readline().split()))
result = []

for num in list2:
    if num in list1:
        result.append("1")
    else:
        result.append("0")

print(' '.join(result))