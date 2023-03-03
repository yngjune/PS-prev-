from sys import stdin

N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int, stdin.readline().split())

dp = [0] * N
for i in range(N):
    if T[0] - 1 <= i:
        dp[i] = P[0]
    for j in range(1, i+1):
        if j + T[j] - 1 <= i:
            dp[i] = max(dp[i], dp[j-1] + P[j])

print(max(dp))