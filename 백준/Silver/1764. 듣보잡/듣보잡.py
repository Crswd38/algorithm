from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
d = {}
b = {}
db = {}

for i in range(n):
    d[input().strip()] = 0
for _ in range(m):
    a = input().strip()
    if a in d:
        db[a] = 0

print(len(db))
for i in sorted(db.keys()):
    print(i)