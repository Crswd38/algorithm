def solution(elements):
    s = set()
    elementLen = len(elements)
    elements *= 2

    for i in range(elementLen):
        for j in range(elementLen):
            s.add(sum(elements[j:i+j+1]))
    return len(s)