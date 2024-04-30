n, k = map(int, input().split())
sum = 0
a = []

for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)

for i in a:
    if k // i != 0:
        sum += k // i
        k %= i
print(sum)