from sys import stdin
input = stdin.readline

arr = [0]*10
a = int(input())
b = int(input())
c = int(input())

for i in str(a*b*c):
    arr[int(i)] += 1

for i in arr:
    print(i)