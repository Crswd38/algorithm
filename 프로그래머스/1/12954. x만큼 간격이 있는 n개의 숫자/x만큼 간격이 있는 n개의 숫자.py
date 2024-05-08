def solution(x, n):
    return [0]*n if x == 0 else [i for i in range(x, x*n+x, x)]