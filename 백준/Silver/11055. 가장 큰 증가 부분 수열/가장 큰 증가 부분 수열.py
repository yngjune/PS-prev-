N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

dp[0] = arr[0]
for i in range(1,N):
    for j in range(i):
        if arr[j] >= arr[i]:
            continue
        dp[i] = max(dp[i], dp[j])
    dp[i] += arr[i]

print(max(dp))