def solution(n):
    dp = [0,1]
    for i in range(2, n+1):
        dp.append((dp[-1] + dp[-2])%1234567)
    return dp[n]