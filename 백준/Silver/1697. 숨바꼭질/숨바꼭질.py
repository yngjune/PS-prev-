from collections import deque
MAX_POS = 100000

N, K = map(int, input().split())
queue = deque()
queue.append((N, 0))

visit = [False] * (MAX_POS + 1)
visit[N] = True

while queue:
    cur = queue.popleft()
    if cur[0] == K:
        print(cur[1])
        break

    next = cur[0] - 1
    if next >= 0 and not visit[next]:
        queue.append((next, cur[1]+1))
        visit[next] = True
    
    next = cur[0] + 1
    if next <= MAX_POS and not visit[next]:
        queue.append((next, cur[1]+1))
        visit[next] = True
    
    next = cur[0] * 2
    if next <= MAX_POS and not visit[next]:
        queue.append((next, cur[1]+1))
        visit[next] = True