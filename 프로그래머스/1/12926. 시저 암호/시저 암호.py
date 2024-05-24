def solution(s, n):
    a = 0
    li = list(s)
    for i in range(len(li)):
        if li[i] != " ":
            a = (ord(li[i]) + n)
            if a > 122:
                a -= 26
            elif li[i].isupper() and a > 90:
                a -= 26
            li[i] = chr(a)
    return(''.join(li))