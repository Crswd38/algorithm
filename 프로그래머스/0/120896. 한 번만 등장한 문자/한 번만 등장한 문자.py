from collections import Counter

def solution(s):
    return ''.join(sorted([i if j == 1 else "" for i, j in Counter(s).items()]))