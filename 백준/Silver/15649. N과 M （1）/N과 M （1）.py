def comb(depth):
    if depth == M:
        print(*arr[:M])
        return
    
    for i in range(1, N+1):
        if not visit[i]:
            visit[i] = True
            arr[depth] = i
            comb(depth+1)
            visit[i] = False



N, M = map(int, input().split())
visit = [False] * (N + 1)
arr = [0] * N
comb(0)