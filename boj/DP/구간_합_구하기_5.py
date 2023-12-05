from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
query = [list(map(int, stdin.readline().split())) for _ in range(m)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

for a, b, c, d in query:
    print(dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1])