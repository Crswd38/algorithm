def solution(s):
    result = 0
    cnt = 0
    while s != "1":
        result += s.count("0")
        s = bin(len(s.replace("0", "")))[2:]
        cnt += 1
    return [cnt, result]