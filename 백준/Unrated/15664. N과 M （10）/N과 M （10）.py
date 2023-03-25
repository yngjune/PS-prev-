def backtrack(depth, start):
    if depth == M:
        print(*seq)
        return
    
    prev = 0
    for i in range(start,N):
        if visit[i] or prev == arr[i]:
            continue
        visit[i] = True
        prev = arr[i]
        seq[depth] = arr[i]
        backtrack(depth+1, i+1)
        visit[i] = False
        

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visit = [False] * N
seq = [0] * M
backtrack(0, 0)