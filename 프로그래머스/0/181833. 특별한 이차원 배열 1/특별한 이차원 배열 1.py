def solution(n):
    return [[int(j==i) for j in range(n)] for i in range(n)]