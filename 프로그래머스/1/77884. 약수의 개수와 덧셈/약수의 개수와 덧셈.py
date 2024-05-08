def solution(left, right):
    return sum(i if len([1 for j in range(1, i+1) if i%j==0])%2 == 0 else -i for i in range(left, right+1))