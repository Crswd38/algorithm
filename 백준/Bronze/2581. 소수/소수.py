import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

def prime_numbers(m, n):
    arr = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
            
    return [i for i in arr[m:] if arr[i] and arr[i] > 1]

result = prime_numbers(M, N)
if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)