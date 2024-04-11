def solution(my_string, k):
    arr = []
    for _ in range(k):
        arr.append(my_string)
    answer = ''.join(arr)
    return answer