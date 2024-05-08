def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) if [i for i in arr if i % divisor == 0] else [-1]