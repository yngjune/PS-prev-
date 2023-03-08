from sys import stdin

T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, stdin.readline().split()))
    target = int(input())
    # dp[i][j] : ~ith coin, target price j
    dp = [[0] * (target + 1) for _ in range(N)]

    for i in range(N):
        dp[i][0] = 1

    # first coin
    for i in range(1, target+1):
        dp[0][i] = 1 if i % coin[0] == 0 else 0
    
    # else
    for i in range(1, N):
        for j in range(1, target+1):
            cur = 0
            while cur <= j:
                dp[i][j] += dp[i-1][j-cur]
                cur += coin[i]
    
    print(dp[N-1][target])