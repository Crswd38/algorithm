def solution(n):
	cnt = 0
	for i in range(2, n+1):
		if i % 2:
			if (i + 1) // 2 * i > n:
				break
			if (n - (i + 1) // 2 * i) % i == 0:
				cnt += 1
		else:
			if (i+1) * (i//2) > n:
				break
			if (n - (i+1) * (i//2)) % i == 0:
				cnt += 1
	return cnt + 1