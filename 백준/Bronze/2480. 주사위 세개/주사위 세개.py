A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

if(A == B and B == C):
    print(10000 + A * 1000)
elif(A == B):
    print(1000 + A * 100)
elif(B == C):
    print(1000 + B * 100)
elif(C == A):
    print(1000 + C * 100)
elif(A>B>C or A>C>B):
    print(A*100)
elif(B>A>C or B>C>A):
    print(B*100)
elif(C>A>B or C>B>A):
    print(C*100)