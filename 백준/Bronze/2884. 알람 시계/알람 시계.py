A, B = input().split()

A = int(A)
B = int(B)

if(B >= 45):
    print(f"{A} {B-45}")
else:
    if(A>0):
        print(f"{A-1} {B+15}")
    else:
        print(f"{23} {B+15}")