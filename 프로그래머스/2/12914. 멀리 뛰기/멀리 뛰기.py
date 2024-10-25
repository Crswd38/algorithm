def solution(n):
    arr = [0,1,2]
    for i in range(2, n):
        arr.append((arr[i] + arr[i-1]) % 1234567)
    return arr[n]