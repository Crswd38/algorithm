def solution(num, k):
    num=str(num)
    k=str(k)
    if k in num:
        for i in range(len(num)):
            if num[i] == k:
                return int(i)+1
    else:
        return -1