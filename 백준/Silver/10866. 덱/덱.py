import sys
from collections import deque

N = int(sys.stdin.readline())
deque = deque()

for i in range(N):
    A = sys.stdin.readline().split()

    if A[0] == "push_front":
        deque.appendleft(A[1])

    elif A[0] == "push_back":
        deque.append(A[1])

    elif A[0] == "pop_front":
        if len(deque) != 0:
            print(deque.popleft())
        else:
            print(-1)

    elif A[0] == "pop_back":
        if len(deque) != 0:
            print(deque.pop())
        else:
            print(-1)

    elif A[0] == "size":
        print(len(deque))

    elif A[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif A[0] == "front":
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)

    elif A[0] == "back":
        if len(deque) != 0:
            print(deque[len(deque)-1])
        else:
            print(-1)