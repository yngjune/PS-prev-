def backtrack(depth, start):
    if depth == M:
        print(*sequence)
        return
    
    for i in range(start, N+1):
        if visit[i]:
            continue
        visit[i] = True
        sequence[depth] = i
        backtrack(depth + 1, i + 1)
        visit[i] = False

N, M = map(int, input().split())
sequence = [0] * M
visit = [False] * (N + 1)
backtrack(0, 1)