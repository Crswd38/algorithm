import sys

N = int(sys.stdin.readline().strip())
layer = 1
count = 1

while N > count:
    count += 6 * layer
    layer += 1

print(layer)