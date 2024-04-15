def solution(arr, queries):
    t = 0
    for i in range(len(queries)):
        t = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = t
    return arr