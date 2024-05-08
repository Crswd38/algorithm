def solution(n):
    n -= 1
    i = 2
    while n >= i:
        if n % i == 0:
            return i
        else:
            i += 1