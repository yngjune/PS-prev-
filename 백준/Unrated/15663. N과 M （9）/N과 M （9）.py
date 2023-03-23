def backtrack(depth):
    if depth == M:
        print(*seq)
        return
    prev = []
    for i in range(N):
        if visit[i] or (prev and prev[-1] == arr[i]):
            continue
        visit[i] = True
        seq[depth] = arr[i]
        prev.append(seq[depth])
        backtrack(depth+1)
        visit[i] = False

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visit = [False] * N
seq = [0] * M
backtrack(0)