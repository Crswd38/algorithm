def solution(rank, attendance):
    arr = sorted([rank[i] for i in range(len(rank)) if attendance[i]])
    return 10000 * rank.index(arr[0]) + 100 * rank.index(arr[1]) + rank.index(arr[2])