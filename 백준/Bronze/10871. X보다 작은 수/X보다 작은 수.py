import sys

A, B = sys.stdin.readline().split()
C = sys.stdin.readline().split()
sum = []

for i in range(int(A)):
    if(int(B) > int(C[i])):
        sum.append(C[i]+" ")
print(''.join(sum))