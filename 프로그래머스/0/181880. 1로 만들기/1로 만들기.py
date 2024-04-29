def solution(num_list):
    cnt = 0
    for i in num_list:
        while(i != 1):
            i //= 2
            cnt += 1
    return cnt