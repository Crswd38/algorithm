from math import factorial
    
def solution(balls, share):
    return round(factorial(balls) / (factorial(balls - share) * factorial(share)))
    