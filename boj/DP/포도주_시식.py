from sys import stdin

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]

dp[0][1] = arr[0]
for i in range(1, n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = arr[i] + dp[i-1][0]
    dp[i][2] = arr[i] + dp[i-1][1]
print(max(dp[n-1]))