def solution(N, stages):
    di = dict()
    failPer = 0

    for i in range(N):
        di[i+1] = 0
    for i in stages:
        if i != N+1:
            di[i] = di[i] + 1

    for i in range(N):
        failPer += di[i+1]
        if (len(stages) - failPer + di[i+1]):
            di[i+1] /= (len(stages) - failPer + di[i+1])
        else:
            di[i+1] = 0
            
    arr = sorted(di.items(), reverse=True, key=lambda item:item[1])
    for _ in arr:
        arr = dict(arr)
    return list(arr.keys())