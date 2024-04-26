def solution(num_list):
    return sum(num_list[1::2]) if sum(num_list[1::2]) >= sum(num_list[::2]) else sum(num_list[::2])