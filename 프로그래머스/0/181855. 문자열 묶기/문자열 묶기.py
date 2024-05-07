def solution(strArr):
    arr = [0] * 31
    for i in strArr:
        arr[len(i)] += 1
    return max(arr)