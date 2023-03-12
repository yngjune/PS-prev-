arr = [0] + list(map(int, list(input())))
l = len(arr) - 1
dp = [0] * 5050
MOD = 1000000

dp[0] = 1
for i in range(1,l+1):
    if arr[i] > 0:
        dp[i] = (dp[i] + dp[i-1]) % MOD
    if 10 <= arr[i-1] * 10 + arr[i] <= 26:
        dp[i] = (dp[i] + dp[i-2]) % MOD

print(dp[l])