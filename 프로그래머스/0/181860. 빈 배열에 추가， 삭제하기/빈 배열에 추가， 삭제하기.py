def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if flag[i]:
            for _ in range(arr[i]*2):
                X.append(arr[i])
        else:
            for _ in range(arr[i]):
                X.pop()
    return X