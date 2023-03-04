from sys import stdin
N = int(input())
M = int(input())
div = [0] + [int(stdin.readline()) for _ in range(M)] + [N+1]

dp = [1] * 45
dp[2] = 2
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
for i in range(1,len(div)):
    ans *= (dp[div[i] - div[i-1] - 1])

print(ans)