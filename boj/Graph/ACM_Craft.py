from sys import stdin
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    N, K = map(int, stdin.readline().split())
    cost = [0] + list(map(int, stdin.readline().split()))
    edge = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    for _ in range(K):
        u, v = map(int, stdin.readline().split())
        edge[u].append(v)
        indegree[v] += 1
    target = int(stdin.readline())

    queue = deque()
    depth = [-1 for _ in range(N+1)]
    max_acc = [0 for _ in range(N+1)]

    for u in range(1, N+1):
        if indegree[u] == 0:
            queue.append(u)
            depth[u] = 0
            max_acc[u] = cost[u]
    
    while queue:
        x = queue.popleft()
        d = depth[x]
        
        for v in edge[x]:
            indegree[v] -= 1
            if indegree[v] == 0:
                depth[v] = d + 1
                queue.append(v)
            if max_acc[x] + cost[v] > max_acc[v]:
                max_acc[v] = max_acc[x] + cost[v]

    print(max_acc[target])