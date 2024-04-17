def solution(emergency):
    arr = sorted(emergency, reverse=True)
    result = []
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if emergency[i] == arr[j]:
                result.append(j+1)
    return result

