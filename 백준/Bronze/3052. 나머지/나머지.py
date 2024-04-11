import sys

number = set()

for _ in range(10):
    j = int(sys.stdin.readline())
    number.add(j % 42)

print(len(number))