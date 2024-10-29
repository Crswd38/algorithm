import math

def solution(n,a,b):
    cnt = 0

    while a != b:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        cnt += 1

    return cnt