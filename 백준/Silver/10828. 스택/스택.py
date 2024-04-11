import sys

N = int(sys.stdin.readline())   
stack = []

for i in range(N):
    A = sys.stdin.readline().split()
    if A[0] == "push":
        stack.append(A[1])
    elif A[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif A[0] == "size":
        if len(stack) == 0:
            print(0)
        else:
            print(len(stack))
    elif A[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif A[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])