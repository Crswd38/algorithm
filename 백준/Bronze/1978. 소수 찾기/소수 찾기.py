import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
cnt = 0

def is_prime(num):
    if num < 2:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1

for i in numbers:
	cnt += is_prime(i)
print(cnt)
