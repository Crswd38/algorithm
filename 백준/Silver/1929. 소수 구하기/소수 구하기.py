import sys

M, N = map(int, sys.stdin.readline().split())

def sieve_of_eratosthenes(M, N):
    primes = []
    is_prime = [True] * (N+1)
    is_prime[0] = is_prime[1] = False

    if M == 1:
        M += 1

    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N+1, i):
                is_prime[j] = False
    primes = [num for num in range(M, N+1) if is_prime[num]]
    return primes

prime = sieve_of_eratosthenes(M, N)
for i in prime:
    print(i)
