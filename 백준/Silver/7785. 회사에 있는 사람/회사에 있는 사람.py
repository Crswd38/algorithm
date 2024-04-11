import sys

N = int(sys.stdin.readline().strip())
S = set()
sum = 0 
A = []

for _ in range(N):
    a, b = sys.stdin.readline().split()
    if(b == "enter"):
        S.add(a)
    elif(b == "leave"):
        S.discard(a)

sorted_list = sorted(S, reverse=True)
print('\n'.join(sorted_list))