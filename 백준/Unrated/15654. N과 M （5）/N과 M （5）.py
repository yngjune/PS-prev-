def backtrack(depth):
    if depth == M:
        print(*sequence)
        return
    
    for i in range(N):
        if visit[i]:
            continue
        visit[i] = True
        sequence[depth] = arr[i]
        backtrack(depth + 1)
        visit[i] = False

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
sequence = [0] * M
visit = [False] * (N + 1)
backtrack(0)