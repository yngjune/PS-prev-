from collections import deque
MAX = 100000

N, K = map(int, input().split())
queue = deque()
depth = [-1] * (MAX + 1)

queue.append(N)
depth[N] = 0
while queue:
    cur = queue.popleft()
    if cur == K:
        print(depth[cur])
        break

    next = cur * 2
    if 0 <= next <= MAX and depth[next] == -1:
        queue.appendleft(next)
        depth[next] = depth[cur]
    
    for dx in [-1, 1]:
        next = cur + dx
        if 0 <= next <= MAX and depth[next] == -1:
            queue.append(next)
            depth[next] = depth[cur] + 1
