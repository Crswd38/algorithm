def solution(t, p):
    return sum(1 for i in range(0, len(t) - len(p) + 1) if int(t[i:i+len(p)]) <= int(p))