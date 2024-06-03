def solution(answers):
	arr = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
	result = [0] * len(arr)

	for a, b in enumerate(answers):
		for c, d in enumerate(arr):
			if b == d[a % len(d)]:
				result[c] += 1
	return [c + 1 for c, d in enumerate(result) if d == max(result)]