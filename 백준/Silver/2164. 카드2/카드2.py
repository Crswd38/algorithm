import sys

N = int(sys.stdin.readline())
cnt = 0
index = 1
for _ in range(N):
	if index == 2**cnt + 2:
		index = 2
		cnt += 1
	index += 2
print(index-2)