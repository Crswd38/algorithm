def solution(k, score):
    zundang = []
    result = []
    for i in score:
        if len(zundang) >= k:
            if min(zundang) < i:
                zundang.remove(min(zundang))
                zundang.append(i)
        else:
            zundang.append(i)
        result.append(min(zundang))
    return result