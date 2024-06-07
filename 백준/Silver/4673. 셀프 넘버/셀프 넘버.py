arr = [0 for _ in range(20000)]
for i in range(1, 9981):
    arr[i + sum(int(i) for i in str(i))] = 1
for i in range(1, 10001):
    if arr[i] == 0:
        print(i)