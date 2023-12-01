from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [0 for _ in range(n+1)]
maxlis = 0

for num in arr:
    dp[num] = dp[num-1] + 1
    if dp[num] > maxlis:
        maxlis = dp[num]

print(n - maxlis)