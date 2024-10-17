from math import ceil

def solution(n, words):
    answer = []
    word = [words[0][0]]
    for i in words:
        if i in word or word[len(word)-1][-1] != i[0]:
            return [l%n, ceil(l/n)] if (l:=(len(word)))%n != 0 else [n, ceil(l//n)]
        else:
            word.append(i)
    return [0,0]