from collections import deque

F, S, G, U, D = map(int, input().split())
depth = [-1] * (F + 1)
queue = deque([S])
depth[S] = 0

while queue:
    cur = queue.popleft()
    if cur == G:
        print(depth[cur])
        break
    
    up = cur + U
    down = cur - D

    if up <= F and depth[up] == -1:
        queue.append(up)
        depth[up] = depth[cur] + 1
    
    if down >= 1 and depth[down] == -1:
        queue.append(down)
        depth[down] = depth[cur] + 1
else:
    print("use the stairs")