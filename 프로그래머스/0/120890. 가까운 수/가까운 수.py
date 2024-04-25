def solution(array, n):
    result = 100
    for i in sorted(array):
        if abs(n - result) > abs(n - i):
            result = i
    return result