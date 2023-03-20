from sys import stdin

N = int(input())
arr = [0] + [int(stdin.readline()) for _ in range(N)]

dp = [0] * (N + 1)
if N < 3:
    print(sum(arr))
else:
    dp[1] = arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, N + 1):
        dp[i] = max(arr[i-1] + arr[i] + dp[i-3], dp[i-2] + arr[i], dp[i-1])

    print(dp[N])