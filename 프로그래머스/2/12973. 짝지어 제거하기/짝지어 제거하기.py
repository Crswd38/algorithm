def solution(s):
    answer = 0
    stackS = []
    
    for i in range(len(s)):
        if len(stackS) == 0:
            stackS.append(s[i])
        elif stackS[-1] == s[i]:
            stackS.pop()
        else:
            stackS.append(s[i])
    if len(stackS) == 0:
        return 1
    
    return answer