def solution(number, limit, power):
    sum = 0
    result = 0
    for i in range(1, number+1):
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                sum += 1
                if j**2 != i:
                    sum += 1
        result += power if sum > limit else sum
        sum = 0
    return result