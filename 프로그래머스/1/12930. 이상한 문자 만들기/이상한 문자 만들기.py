def solution(s):
    result = ""
    for i in s.split(" "):
        for j in range(len(i)):
            if j%2:
                result += i[j].lower()
            else:
                result += i[j].upper()
        result += " "
    return result[:-1]