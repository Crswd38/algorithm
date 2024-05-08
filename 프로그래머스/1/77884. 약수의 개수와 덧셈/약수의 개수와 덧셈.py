def solution(left, right):
    return sum(i if (i ** 0.5) % 1 else -i for i in range(left, right+1))