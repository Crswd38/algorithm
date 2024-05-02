def solution(polynomial):
    arr = polynomial.split()
    x = 0
    c = 0
    for i in range(0, len(arr), 2):
        if arr[i][-1] == "x":
            if arr[i][:-1]:
                x += int(arr[i][:-1])
            else:
                x += 1
        else:
            if arr[i]:
                c += int(arr[i])
    if x == 0:
        return str(c)
    elif x == 1 and c == 0:
        return "x"
    elif c == 0:
        return str(x) + "x"
    elif x == 1:
        return "x + " + str(c)
    else:
        return str(x) + "x + " + str(c)