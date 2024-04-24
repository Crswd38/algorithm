def solution(s):
    arr = list(map(int, s.split()))
    a = max(arr)
    b = min(arr)
    return str(min(arr)) + " " + str(max(arr))