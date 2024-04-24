def solution(arr):
    start = -1
    end = 0
    for i in range(len(arr)):
        if arr[i] == 2:
            if start == -1:
                start = i
            end = i
    return [-1] if start == -1 else arr[start:end+1]