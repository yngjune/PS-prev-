n = int(input())
k = int(input())
MOD = 1000000003

dp = [[0 for _ in range(1001)] for _ in range(1001)]
for i in range(1, n+1):
    dp[i][1] = i

for i in range(4, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % MOD

print(dp[n][k])