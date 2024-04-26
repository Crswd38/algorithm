def solution(numbers, n):
    for i in range(len(numbers)):
        if sum(numbers[:i]) > n:
            return sum(numbers[:i])
    return sum(numbers)