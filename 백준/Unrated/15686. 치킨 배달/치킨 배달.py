from sys import stdin

def chicken_distance(i,j):
    ans = 2 * N
    for k in range(C):
        if combination[k]:
            ans = min(ans, abs(i-chicken[k][0]) + abs(j-chicken[k][1]))
    return ans


def sum_chicken_distance():
    ans = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                ans += chicken_distance(i,j)
    return ans


def backtrack(depth, start):
    if depth == M:
        global ans
        ans = min(ans, sum_chicken_distance())
        return
    
    for i in range(start, C):
        combination[i] = True
        backtrack(depth+1, i+1)
        combination[i] = False


N, M = map(int, input().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

C = 0
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            C += 1
            chicken.append((i,j))

combination = [False] * C
ans = 4 * N * N
backtrack(0,0)
print(ans)