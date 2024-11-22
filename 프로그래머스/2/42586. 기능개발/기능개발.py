import math

def solution(progresses, speeds):
    answer = []
    day = []
    num = 0
    cnt = 1

    for i in range(len(progresses)):
        day.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    num = day[0]

    for i in range(1, len(progresses)):
        if day[i] > num:
            num = day[i]
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    
    return answer