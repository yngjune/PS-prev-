from sys import stdin

n = int(stdin.readline())
cost = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]

R = 0
G = 1
B = 2
dp[0][R], dp[0][G], dp[0][B] = cost[0][R], cost[0][G], cost[0][B]

for i in range(1, n):
    dp[i][R] = cost[i][R] + min(dp[i-1][G], dp[i-1][B])
    dp[i][G] = cost[i][G] + min(dp[i-1][R], dp[i-1][B])
    dp[i][B] = cost[i][B] + min(dp[i-1][R], dp[i-1][G])

print(min(dp[n-1]))