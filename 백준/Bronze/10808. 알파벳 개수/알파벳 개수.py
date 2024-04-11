import sys

S = sys.stdin.readline().strip()
alpha = "abcdefghijklmnopqrstuvwxyz"
result = [0] * 26

for i in alpha:
    for j in S:
        if j == i:
            result[alpha.index(i)] += 1

print(' '.join(map(str, result)))