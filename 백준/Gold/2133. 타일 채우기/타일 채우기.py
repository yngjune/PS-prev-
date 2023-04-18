N = int(input())

dp = [0] * 31
dp[0] = 1

for i in range(2, 31, 2):
    dp[i] = 3 * dp[i-2]
    for j in range(i-4, -1, -2):
        dp[i] += 2 * dp[j]

print(dp[N])