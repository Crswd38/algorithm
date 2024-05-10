from sys import stdin
input = stdin.readline

t = list(map(int, input().split()))
arr = dict()
for _ in range(t[0]):
    k, v = input().split()
    arr[k] = v
for _ in range(t[1]):
    print(arr[input().strip()])