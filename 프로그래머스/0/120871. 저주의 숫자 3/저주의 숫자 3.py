def solution(n):
    arr = []
    i = 0
    while len(arr) <= n-1:
        if "3" in str(i):
            i += 1
            continue
        elif i % 3 == 0:
            i += 1
            continue
        else:
            arr.append(i)
            i += 1
    return arr[-1]