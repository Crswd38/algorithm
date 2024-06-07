import sys
input = sys.stdin.readline
n = int(input())
dict = {}
for i in range(n):
    dict[i] = int(input())
for i in sorted(dict.values()):
    print(i)