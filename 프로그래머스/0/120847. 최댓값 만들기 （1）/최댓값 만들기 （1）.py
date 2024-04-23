def solution(numbers):
    a = max(numbers)
    numbers.remove(a)
    b = max(numbers)
    return a * b