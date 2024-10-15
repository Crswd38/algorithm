def solution(k, score):
    zundang = []
    result = []
    for i in score:
        zundang.append(i)
        if len(zundang) > k:
            zundang.remove(min(zundang))
        result.append(min(zundang))
    return result