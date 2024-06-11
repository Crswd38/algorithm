from itertools import permutations

def solution(spell, dic):
    for i in list(permutations(spell, len(spell))):
        if ''.join(i) in dic:
            return 1
    return 2