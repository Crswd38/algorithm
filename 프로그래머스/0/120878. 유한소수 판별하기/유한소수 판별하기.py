from math import gcd
def solution(a, b):
    arr = []
    i = 2
    if gcd(a, b) != 1:
        a, b = a//gcd(a, b), b//gcd(a, b)
    while b >= i:
        if b % i == 0:
            arr.append(i)
            b /= i
        else:
            i += 1
    return 1 if len(arr) == arr.count(2) + arr.count(5) else 2
        
    
    