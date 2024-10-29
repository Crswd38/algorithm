def solution(citations):
    answer = 0
    n = len(citations)

    for i in range(len(citations)):
        h = n - i
        if sum(1 for j in citations if j >= h) >= h:
            answer = h
            break
    return answer