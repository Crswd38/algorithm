import math
import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a, b))