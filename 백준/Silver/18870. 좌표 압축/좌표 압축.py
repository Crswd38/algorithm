from sys import stdin
input = stdin.readline

n = int(input().strip())
x = list(map(int, input().split()))
dict = {}

arr = sorted(set(x))
dict = {arr[i] : i for i in range(len(arr))}

for i in x:
    print(dict[i], end=" ")