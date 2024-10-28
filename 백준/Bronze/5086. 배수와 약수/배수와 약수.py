import sys

while True:
    first, second = map(int, sys.stdin.readline().split())
    if first == 0 and second == 0:
        break
    elif second % first == 0:
        print("factor")
    elif first % second == 0:
        print("multiple")
    else:
        print("neither")