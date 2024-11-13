def solution(s):
    answer = 0
    circle = s*2

    for i in range(len(s)):
        sub = circle[i:i+len(s)]
        stack = []
        for j in sub:
            if not stack :
                stack.append(j)
                continue
            if ((stack[-1]=='['and j==']') or
                (stack[-1]=='('and j==')') or
                (stack[-1]=='{'and j=='}')):
                stack.pop()
            else:
                stack.append(j)
        answer += 1 if not stack else 0
    return answer