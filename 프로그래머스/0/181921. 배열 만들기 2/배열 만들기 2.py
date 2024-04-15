def solution(l, r):
    result = []
    for i in range(l, r+1):
        if not set(str(i)) - set(['0', '5']):
            result.append(i)
            
    return result if result else [-1]
