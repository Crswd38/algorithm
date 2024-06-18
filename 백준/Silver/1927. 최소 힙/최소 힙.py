from sys import stdin
import heapq

input = stdin.readline

heap = []

for _ in range(int(input())):
    if 0 == (x := int(input())):
        print(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, x)