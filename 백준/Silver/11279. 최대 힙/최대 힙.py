import heapq
from sys import stdin
input = stdin.readline

heap = []

for _ in range(int(input())):
    if 0 == (x := int(input())):
        print(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, (-x, x))