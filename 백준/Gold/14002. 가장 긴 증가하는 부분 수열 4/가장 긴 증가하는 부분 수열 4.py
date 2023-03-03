from sys import stdin

N = int(input())
arr = list(map(int,stdin.readline().split()))
dp = [1] * N
prev = [-1] * N
max_idx = 0

for i in range(1,N):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] >= dp[i]:
            prev[i] = j
            dp[i] = dp[j] + 1

    if dp[i] > dp[max_idx]:
        max_idx = i

print(dp[max_idx])
stk = []
while max_idx != -1:
    stk.append(arr[max_idx])
    max_idx = prev[max_idx]

print(*stk[::-1])