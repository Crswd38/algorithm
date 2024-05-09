def solution(price, money, count):
    return 0 if (count*(price+count*price))//2 - money <= 0 else (count*(price+count*price))//2 - money