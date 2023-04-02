from sys import stdin

N, K = map(int, input().split())
coin = [int(stdin.readline()) for _ in range(N)]
dp = [0] * (K + 1)

for c in coin:
    if c > K: break
    dp[c] = 1

for i in range(1, K+1):
    for c in coin:
        if i - c < 0 or dp[i-c] == 0:
            continue
        if dp[i] == 0:
            dp[i] = dp[i-c] + 1
        else:
            dp[i] = min(dp[i], dp[i-c] + 1)
if dp[K] == 0:
    print(-1)
else:
    print(dp[K])