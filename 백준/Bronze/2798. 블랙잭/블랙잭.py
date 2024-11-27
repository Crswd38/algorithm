from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

combi = list(map(sum, combinations(arr, 3)))

print(sorted(combi, key=lambda x: (M-x) if M >= x else 100000)[0])