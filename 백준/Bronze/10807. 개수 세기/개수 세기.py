import sys

A = int(sys.stdin.readline())
B = sys.stdin.readline().split()
C = int(sys.stdin.readline())
sum = 0

for i in range(A):
    if(C == int(B[i])):
        sum += 1

print(sum)