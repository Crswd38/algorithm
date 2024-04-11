import sys

number = [False] * 30
A = 0

for _ in range(28):
    i = int(sys.stdin.readline())
    number[i-1] = True

for i in range(30):
    if(number[i] != True):
        print(i+1)