def solution(arr, queries):
    result = []
    for s, e, k in queries:
        a = []
        for i in range(s, e+1):
            if arr[i] > k:
                a.append(arr[i])
        if a:
            result.append(min(a))
        else:
            result.append(-1)
    return result