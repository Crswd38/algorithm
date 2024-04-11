import sys

x, y, w, h = map(int, sys.stdin.readline().split())

r = [x, y, w-x, h-y]

print(min(r))