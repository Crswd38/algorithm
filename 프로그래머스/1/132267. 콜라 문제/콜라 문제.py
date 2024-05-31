def solution(a, b, n):
    c = 0
    result = 0
    while (n + c) // a > 0:
        n, c = (n + c) // a * b, (n + c) % a
        print(n,c)
        result += n
    return result