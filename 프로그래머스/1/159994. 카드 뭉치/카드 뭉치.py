from collections import deque

def solution(c1, c2, goal):
    c1 = deque(c1)
    c2 = deque(c2)

    for i in range(len(goal)):
        if c1 and goal[i] == c1[0]:
            c1.popleft()
        elif c2 and goal[i] == c2[0]:
            c2.popleft()
        else:
            return "No"
    return "Yes"