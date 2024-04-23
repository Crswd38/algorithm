def solution(my_string):
    result = []
    for i in range(1, len(my_string)+1):
        result.append(my_string[-i:])
    result.sort()
    return result