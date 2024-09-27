def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    for _ in(range(4 - len(answer))):
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer