from collections import Counter

def solution(array):
    data = Counter(array).most_common(2)
    if len(data) == 1:
        return data[0][0]
    elif data[0][1] == data[1][1]:
        return -1
    return data[0][0]

