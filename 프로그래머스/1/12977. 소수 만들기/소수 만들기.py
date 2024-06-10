from itertools import combinations

def solution(nums):
    return sum(is_prime_number(i) for i in list(map(sum, combinations(nums, 3))))

def is_prime_number(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return 0
    return 1
