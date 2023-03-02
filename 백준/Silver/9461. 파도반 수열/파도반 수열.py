MAX = 100

dp = [0, 1, 1, 1, 2, 2] + [0] * MAX
for i in range(6, MAX + 1):
    dp[i] = dp[i-1] + dp[i-5]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])