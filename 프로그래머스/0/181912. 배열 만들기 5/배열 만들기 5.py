def solution(intStrs, k, s, l):
    result = []
    for i in intStrs:
        i = str(i)
        if int(i[s:s+l]) > k:
            result.append(int(i[s:s+l]))
    return result