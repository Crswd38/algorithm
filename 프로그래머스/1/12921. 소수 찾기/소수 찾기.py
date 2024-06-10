def solution(n):

    return sum(is_prime_number(i) for i in range(2, n+1))

def is_prime_number(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return 0
    return 1