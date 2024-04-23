def solution(my_string, is_suffix):
    arr = []
    for i in range(1, len(my_string)+1):
        arr.append(my_string[-i:])
    if is_suffix in arr:
        return 1
    return 0