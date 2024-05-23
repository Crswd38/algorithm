def l4seat(n, m):
    if n < 12 or m < 4:
        return -1
    return m * 11 + 4

T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    print(l4seat(n, m))