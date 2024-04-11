import sys

max2 = 0
max = -1000000


for i in range(9):
    A = int(sys.stdin.readline())
    if(max < A):
        max = A
        max2 = i+1
print(max)
print(max2)