from sys import stdin

N = int(input())
triangle = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[0] * (i+1) for i in range(N)]

dp[0][0] = triangle[0][0]
for i in range(1, N):
    dp[i][0] = triangle[i][0] + dp[i-1][0]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]

print(max(dp[N-1]))