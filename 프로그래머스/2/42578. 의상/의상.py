def solution(clothes):
    answer = 1
    di = {}

    for i, j in clothes:
        if j in di:
            di[j].append(i)
        else:
            di[j] = [i]
    
    for i in di.values():
        answer *= len(i)+1

    return answer - 1