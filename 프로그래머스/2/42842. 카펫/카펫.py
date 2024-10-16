def solution(brown, yellow):
    cnt = brown + yellow

    for i in range(3, cnt):
        for j in range(3, i+1):
            if cnt < i * j:
                break
            if cnt == i * j and (i-2) * (j-2) == yellow:
                return [i, j]