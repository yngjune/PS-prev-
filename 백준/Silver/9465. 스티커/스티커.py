from sys import stdin

T = int(input())
for _ in range(T):
    N = int(input())
    score = [list(map(int, stdin.readline().split())) for _ in range(2)]
    dp = [[0] * 3 for _ in range(N)]

    dp[0][1] = score[0][0]
    dp[0][2] = score[1][0]
    for i in range(1, N):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = max(dp[i-1][2], dp[i-1][0]) + score[0][i]
        dp[i][2] = max(dp[i-1][1], dp[i-1][0]) + score[1][i]
    
    print(max(dp[N-1]))