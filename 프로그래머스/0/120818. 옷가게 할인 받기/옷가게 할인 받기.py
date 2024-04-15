from math import floor
def solution(price):
    if price >= 500000 :
        price -= price / 100 * 20
    elif price >= 300000 :
        price -= price / 100 * 10
    elif price >= 100000 :
        price -= price / 100 * 5
    price = floor(price)
    return price