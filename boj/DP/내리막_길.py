from sys import stdin

r, c = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(r)]
dp = [[-1 for _ in range(c)] for _ in range(r)]
ans = 0

adj = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def dfs(x, y):
    if x == r-1 and y == c-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]

    way = 0

    for dx, dy in adj:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny  < 0 or nx >= r or ny >= c:
            continue
        if board[nx][ny] < board[x][y]:
            way += dfs(nx, ny)

    dp[x][y] = way
    return dp[x][y]

print(dfs(0, 0))