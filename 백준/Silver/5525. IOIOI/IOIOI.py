from sys import stdin
input = stdin.readline

n = int(input().strip())
m = int(input().strip())
s = input().strip()
sum = 0

for i in range(len(s) - 1+2*n):
    if s[i : i+1+2*n] == "I" + "OI" * n:
        sum += 1

print(sum)