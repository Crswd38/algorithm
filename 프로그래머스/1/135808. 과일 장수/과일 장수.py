def solution(k, m, score):
    score.sort()
    return sum(score[i * m + len(score) % m] * m for i in range(len(score) // m))
