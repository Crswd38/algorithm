def solution(order):
    return sum([str(order).count(i) for i in '369'])