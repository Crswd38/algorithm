def solution(l, r):
    result = []
    for i in range(l, r+1):
        if "1" not in str(i):
            if "2" not in str(i):
                if "3" not in str(i):
                    if "4" not in str(i):
                        if "6" not in str(i):
                            if "7" not in str(i):
                                if "8" not in str(i):
                                    if "9" not in str(i):
                                        result.append(i)
    if not result:
        result.append(-1)
    return result