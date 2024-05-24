def solution(sizes):
    a = max([sizes[i][0] if sizes[i][0] >= sizes[i][1] else sizes[i][1] for i in range(len(sizes))])
    b = max([sizes[i][1] if sizes[i][0] >= sizes[i][1] else sizes[i][0] for i in range(len(sizes))])
    return a*b