from collections import Counter
def solution(s):
    arr = Counter(s.lower())
    return arr['p'] == arr['y']