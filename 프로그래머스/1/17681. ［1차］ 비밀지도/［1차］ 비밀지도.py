def solution(n, arr1, arr2):
    arr = ["" for _ in range(n)]
    str = ""
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:].rjust(n, "0")
        arr2[i] = bin(arr2[i])[2:].rjust(n, "0")
    for i in range(n):
        for j in range(n):
            if int(arr1[i][j]) or int(arr2[i][j]):
                str += "#"
            else:
                str += " "
        arr[i] = str
        str = ""
    return arr