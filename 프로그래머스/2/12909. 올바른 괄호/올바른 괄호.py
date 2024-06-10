def solution(s):
    num = 0
    for i in s:
        num += 1 if i == "(" else -1
        if num < 0:
            return False
    return True if num == 0 else False