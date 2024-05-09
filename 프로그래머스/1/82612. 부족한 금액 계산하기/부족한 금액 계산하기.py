def solution(price, money, count):
    return max(0, count * (price + count * price) // 2 - money)