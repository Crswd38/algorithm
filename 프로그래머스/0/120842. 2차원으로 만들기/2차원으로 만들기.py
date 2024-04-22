def solution(num_list, n):
    return [[j for j in num_list[i:i+n]] for i in range(0, len(num_list), n)]