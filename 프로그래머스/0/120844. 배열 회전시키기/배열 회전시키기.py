from collections import deque
def solution(numbers, direction):
    if direction == "right":
        i = numbers.pop()
        numbers.insert(0, i)
    elif direction == "left":
        i = numbers.pop(0)
        numbers.append(i)
    return numbers