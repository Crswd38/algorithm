def solution(array):
    sum = 0
    index = 0
    for i in range(len(array)):
        if array[i] > sum:
            sum = array[i]
            index = i
    return [sum, index]