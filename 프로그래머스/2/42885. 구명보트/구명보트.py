from collections import deque

def solution(people, limit):
    ans = 0
    people.sort()
    people = deque(people)

    while True:
        if len(people) == 1:
            return ans + 1
        elif len(people) < 1:
            return ans
        if people[0] + people[len(people)-1] > limit:
            people.pop()
            ans += 1
        else:
            people.popleft()
            people.pop()
            ans += 1