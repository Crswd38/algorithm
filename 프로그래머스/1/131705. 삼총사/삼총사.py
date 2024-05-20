from itertools import combinations

def solution(number):
    return sum(1 for i,j,k in list(combinations(number, 3)) if i+j+k == 0)