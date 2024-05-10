from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = list(map(int, input().split()))
    print(str((n-1)%h+1) + str((n-1)//h+1).rjust(2, '0'))