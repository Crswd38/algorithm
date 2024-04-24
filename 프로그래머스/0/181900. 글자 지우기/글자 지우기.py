def solution(my_string, indices):
    result = []
    my_string = list(my_string)
    for i in range(len(indices)):
        for j in range(i, len(indices)):
            if indices[j] > indices[i]:
                indices[j] -= 1
        my_string.pop(indices[i])
    return ''.join(my_string)