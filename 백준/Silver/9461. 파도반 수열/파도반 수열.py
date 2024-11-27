from sys import stdin

T = int(stdin.readline())

for _ in range(T):
	arr = [0,1,1,1,2,2,3]
	N = int(stdin.readline()) 
	
	if N <= 6:
		print(arr[N])
	else:
		for i in range(7, N+1):
			arr.append(arr[i-1] + arr[i-5])
		print(arr[N])