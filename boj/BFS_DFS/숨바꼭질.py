from collections import deque
LBOUND = 0
UBOUND = 100000

n, k = map(int, input().split())
depth = [-1 for _ in range(LBOUND, UBOUND+1)]

queue = deque()
queue.append(n)
depth[n] = 0

while queue:
    x = queue.popleft()
    d = depth[x]
    if x == k:
        print(d)
        break

    if x * 2 <= UBOUND and depth[x*2] == -1:
        depth[x*2] = d + 1
        queue.append(x*2)
    if x - 1 >= LBOUND and depth[x-1] == -1:
        depth[x-1] = d + 1
        queue.append(x-1)
    if x + 1 <= UBOUND and depth[x+1] == -1:
        depth[x+1] = d + 1
        queue.append(x+1)
