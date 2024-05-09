def solution(order):
    return sum([4500 if "americano" in i or "anything" in i else 5000 for i in order])