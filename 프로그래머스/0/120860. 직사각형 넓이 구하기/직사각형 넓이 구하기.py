def solution(dots):
    a = 0
    b = 0
    if dots[0][0] - dots[1][0] != 0:
        a = abs(dots[0][0] - dots[1][0])
    else:
        a = abs(dots[0][0] - dots[2][0]);
    if dots[0][1] - dots[1][1] != 0:
        b = abs(dots[0][1] - dots[1][1])
    else:
        b = abs(dots[0][1] - dots[2][1]);
    return a * b