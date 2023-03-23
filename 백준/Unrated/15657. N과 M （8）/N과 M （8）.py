def backtrack(depth, start):
    if depth == M:
        print(*seq)
        return
    
    for i in range(start,N):
        seq[depth] = arr[i]
        backtrack(depth+1,i)

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
seq = [0] * M
backtrack(0, 0)