import sys

T = int(sys.stdin.readline())
sum = 0

for i in range(T):
    A = sys.stdin.readline().strip()
    for j in A:
        if j == "(":
            sum += 1
        elif j == ")":
            sum -= 1
        if sum < 0:
            break
    if sum == 0:
        print("YES")
    else:
        print("NO")
    sum = 0