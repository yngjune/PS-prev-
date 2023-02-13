from sys import stdin
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    graph = [list(stdin.readline()[:-1])for _ in range(H)]

    fire = deque()
    man = deque()

    for i in range(H):
        for j in range(W):
            if graph[i][j] == '@':
                man.append((i,j))
            elif graph[i][j] == '*':
                fire.append((i,j))

    ans = "IMPOSSIBLE"
    depth = 1
    while man:
        for _ in range(len(fire)):
            x, y = fire.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < H and ny >= 0 and ny < W and \
                    (graph[nx][ny] == '.' or graph[nx][ny] == '@'):
                    graph[nx][ny] = '*'
                    fire.append((nx,ny))

        for _ in range(len(man)):
            x, y = man.popleft()
            if x == 0 or x == H-1 or y == 0 or y == W-1:
                ans = depth
                man = None
                break

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < H and ny >= 0 and ny < W and \
                    graph[nx][ny] == '.':
                    graph[nx][ny] = '@'
                    man.append((nx,ny))
        depth += 1

    print(ans)