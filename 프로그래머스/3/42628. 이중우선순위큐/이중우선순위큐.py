def solution(operations):
    queue = []
    for i in operations:
        a, b = i.split()
        b = int(b)
        if a == "I":
            queue.append(b)
        else:
            if b < 0:
                if queue:
                    queue.remove(min(queue))
            else:
                if queue:
                    queue.remove(max(queue))
    return [max(queue),min(queue)] if queue else [0,0]