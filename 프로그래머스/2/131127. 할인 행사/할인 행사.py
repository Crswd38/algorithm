def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        discount_list = discount[i:i+10]
        for j in range(len(want)):
            if discount_list.count(want[j]) != number[j]:
                break
        else:
            answer += 1
    return answer