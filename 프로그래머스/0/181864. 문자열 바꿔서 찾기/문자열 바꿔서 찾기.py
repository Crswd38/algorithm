def solution(myString, pat):
    return 1 if pat in ''.join(['B' if i == 'A' else 'A' for i in myString]) else 0