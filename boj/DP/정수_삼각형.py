from sys import stdin

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(i+1)] for i in range(n)]

for i in range(n):
    dp[n-1][i] = arr[n-1][i]

for i in range(n-2, -1, -1):
    for j in range(i+1):
        dp[i][j] = arr[i][j] + max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])