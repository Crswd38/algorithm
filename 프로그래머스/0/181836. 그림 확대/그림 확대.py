def solution(picture, k):
    result = []
    for i in picture:
        result += [''.join([j * k for j in i])] * k
    return result