def solution(myString, pat):
    return int(''.join(['B' if i == 'A' else 'A' for i in pat]) in myString)