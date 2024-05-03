sum = 0
n = int(input())
p = list(map(int, input().split()))

p.sort()
for i in range(len(p)):
    sum += p[i] * (len(p)-i)
print(sum)