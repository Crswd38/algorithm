from sys import stdin
input = stdin.readline

t = int(input())
dp = [[1,0], [0,1]]
for _ in range(t):
    n = int(input())
    if n == 0:
        print(' '.join(list(map(str, dp[0]))))
    elif n == 1:
        print(' '.join(list(map(str, dp[1]))))
    else:
        for i in range(2, n+1):
            dp.append([dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]])
        print(' '.join(list(map(str, dp[len(dp)-1]))))
    dp = [[1,0], [0,1]]