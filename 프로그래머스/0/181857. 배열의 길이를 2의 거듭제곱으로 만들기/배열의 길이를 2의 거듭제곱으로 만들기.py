def solution(arr):
    for i in range(0, 11):
        print(i)
        if 2**i >= len(arr):
            arr += [0] * (2**i - len(arr))
            return arr