def backtrack(depth, start_idx):
    if depth == M:
        print(*seq)
        return
    
    for i in range(start_idx, N):
        if visit[i]:
            continue
        visit[i] = True
        seq[depth] = arr[i]
        backtrack(depth + 1, i + 1)
        visit[i] = False

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
seq = [0] * M
visit = [False] * N
backtrack(0, 0)