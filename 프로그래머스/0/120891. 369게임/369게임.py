def solution(order):
    return sum([1 for i in str(order) if i == "3" or i == "6" or i == "9"])