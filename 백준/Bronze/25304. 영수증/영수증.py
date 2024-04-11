A = int(input())
B = int(input())
sum = 0

for i in range(B):
    C, D = input().split()
    sum = sum + int(C) * int(D)

if(sum == A):
    print("Yes")
else:
    print("No")