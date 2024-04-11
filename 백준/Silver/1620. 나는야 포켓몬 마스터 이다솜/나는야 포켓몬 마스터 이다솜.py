import sys

N, M = map(int, sys.stdin.readline().split())
S = set()
sum = 0

name_to_number = {}
number_to_name = []

for i in range(1, N + 1):
    name = sys.stdin.readline().strip()
    name_to_number[name] = i
    number_to_name.append(name)

for _ in range(M):
    query = sys.stdin.readline().strip()
    if query.isdigit():
        print(number_to_name[int(query) - 1])
    else:
        print(name_to_number[query])