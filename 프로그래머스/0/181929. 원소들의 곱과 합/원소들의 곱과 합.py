def solution(num_list):
    hap = 0
    mul = 1
    for i in num_list:
        hap += i
        mul *= i
    if hap**2 >= mul:
        return 1
    return 0