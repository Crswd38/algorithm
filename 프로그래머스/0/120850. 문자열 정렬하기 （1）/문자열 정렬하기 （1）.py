def solution(my_string):
    result = []
    for i in my_string:
        if i.isnumeric():
            result.append(int(i))
    result.sort()
    return result