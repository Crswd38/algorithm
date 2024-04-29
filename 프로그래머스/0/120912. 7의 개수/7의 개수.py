def solution(array):
    sum = 0
    array = list(map(str, array))
    for i in array:
        for j in i:
            if j == "7":
                sum += 1
    return sum