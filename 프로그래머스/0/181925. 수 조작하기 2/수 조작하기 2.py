def solution(numLog):
    key = dict(zip([1,-1,10,-10], ['w','s','d','a']))
    result = []
    for i in range(1, len(numLog)):
        result.append(key[numLog[i] - numLog[i-1]])
    return ''.join(result)