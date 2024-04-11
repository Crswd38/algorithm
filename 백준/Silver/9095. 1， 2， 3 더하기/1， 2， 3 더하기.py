import sys

T = int(sys.stdin.readline())
arr = [0, 1, 2, 4]

for _ in range(T):
    n = int(sys.stdin.readline())
    for i in range(4, n+1):
        arr.append(arr[i-1] + arr[i-2] + arr[i-3])
    print(arr[n])
    arr = [0, 1, 2, 4]