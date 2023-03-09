from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
dp = [[True] * N for _ in range(N)]

for diff in range(1, N):
    for i in range(N-diff):
        s, e = i, i + diff
        dp[s][e] = (arr[s] == arr[e]) and dp[s+1][e-1]

M = int(input())
for _ in range(M):
    S, E = map(int, stdin.readline().split())
    print(1 if dp[S-1][E-1] else 0) 