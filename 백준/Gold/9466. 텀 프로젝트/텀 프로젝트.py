import sys
sys.setrecursionlimit(100100)

def DFS(start):
    path.append(start)
    visit[start] = True
    next = graph[start]
    
    if not visit[next]:
        return DFS(next)
    elif next in path:
        return len(path) - path.index(next)

    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visit = [False] * (N+1)
    node_in_cycle = 0
    
    for i in range(1,N+1):
        if not visit[i]:
            path = []
            node_in_cycle += DFS(i)
    
    print(N - node_in_cycle)