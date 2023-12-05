from sys import stdin, maxsize
from heapq import heappush, heappop

V, E = map(int, stdin.readline().split())
S = int(stdin.readline())
edge = [[] for _ in range(V+1)]
dist = [maxsize for _ in range(V+1)]
dist[S] = 0

for _ in range(E):
    u, v, weight = map(int, stdin.readline().split())
    edge[u].append((v, weight))

heap = []
heappush(heap, (0, S))
while heap:
    du, u = heappop(heap)
    
    for v, wv in edge[u]:
        if dist[v] > dist[u] + wv:
            dist[v] = dist[u] + wv
            heappush(heap, (dist[v], v))

for i in range(1, V+1):
    if dist[i] == maxsize:
        print("INF")
    else:
        print(dist[i])