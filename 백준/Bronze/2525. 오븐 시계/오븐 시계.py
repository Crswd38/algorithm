A, B = input().split()
C = input()

A = int(A)
B = int(B)
C = int(C)
D = 0

D = B+C
B = D%60
A = D//60+A
A = A%24

print(f"{A} {B}")