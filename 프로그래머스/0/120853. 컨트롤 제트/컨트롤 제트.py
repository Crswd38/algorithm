def solution(s):
    result = 0
    s = s.split()
    for i in range(len(s)):
        if s[i] == "Z":
            result -= int(s[i-1])
        else:
            result += int(s[i])
            
    return result