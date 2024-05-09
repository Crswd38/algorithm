def solution(arr1, arr2):
    return [[i + j for i, j in zip(sub1, sub2)] for sub1, sub2 in zip(arr1, arr2)]