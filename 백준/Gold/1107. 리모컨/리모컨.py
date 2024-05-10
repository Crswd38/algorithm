from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())
b = set(input().split()) if m else set()
result = abs(100 - n)

for num in range(1000001): 
    for i in str(num):
        if i in b:
            break
    else:
        result = min(result, len(str(num)) + abs(num - n))
print(result)
