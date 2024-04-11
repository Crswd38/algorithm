def solution(code):
    mode = False
    ret = []
    for i in range(len(code)):
        if code[i] == "1":
            if mode:
                mode = False
            else:
                mode = True
        else:
            if mode:
                if i % 2 == 1:
                    ret.append(code[i])
            else:
                if i % 2 == 0:
                    ret.append(code[i])
    answer = ''.join(ret)
    if answer == "":
        return "EMPTY"
    return answer