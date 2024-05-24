def solution(s):
    di = {}
    arr = []
    for i in range(26):
        di[chr(i+97)] = -1
    for i in range(len(s)):
        arr.append(i - di[s[i]] if di[s[i]] != -1 else -1)
        di[s[i]] = i
    return arr