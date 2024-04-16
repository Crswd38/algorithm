def solution(n):
    sum = 0
    for i in range(0, n+1, 2):
        sum += i
    return sum