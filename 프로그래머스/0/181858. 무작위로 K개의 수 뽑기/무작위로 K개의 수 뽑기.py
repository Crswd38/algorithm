def solution(arr, k):
    result = []
    for i in arr:
        if len(result) == k:
            break
        if not i in result:
            result.append(i)
    if len(result) < k:
        for i in range(len(result), k):
            result.append(-1)
    return result