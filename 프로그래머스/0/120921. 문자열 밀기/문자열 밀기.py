def solution(A, B):
    result = 0
    for i in range(len(A)):
        if A == B:
            return result
        A = A[-1] + A[:-1]
        result += 1
    return -1
        
        
    