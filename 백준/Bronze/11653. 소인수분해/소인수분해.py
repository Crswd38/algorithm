import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

N = int(sys.stdin.readline())
while(is_prime(N)):
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print(i)
            N /= i
            break
if N != 1:
    print(int(N))