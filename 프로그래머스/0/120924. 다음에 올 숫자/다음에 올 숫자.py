def solution(c):
    return c[-1]+c[1]-c[0] if c[1]-c[0] == c[2]-c[1] else c[-1]*(c[1]/c[0])
        