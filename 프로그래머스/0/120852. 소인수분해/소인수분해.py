def solution(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return sorted(list(set(factors)))