def solution(n):
    dp = []
    dp.append(0)
    dp.append(1)
    
    for i in range(2, n+1):
        dp.append((dp[-1] + dp[-2])%1234567)
    return dp[n]