from itertools import combinations

n, m = map(int, input().split())
arr = list(combinations([i for i in range(1, n+1)], m))
for i in arr:
	print(' '.join(list(map(str, i))))