def solution(n, k):
    result = 0
    if k - (n//10) < 0:
        result = n * 12000
    else:
        result = n * 12000 + (k - n//10) * 2000
    return result