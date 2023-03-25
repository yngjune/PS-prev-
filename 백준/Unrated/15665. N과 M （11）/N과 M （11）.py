def backtrack(depth):
    if depth == M:
        print(*seq)
        return
    
    prev = 0
    for i in range(N):
        if prev == arr[i]:
            continue
        prev = arr[i]
        seq[depth] = arr[i]
        backtrack(depth+1)
        

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
seq = [0] * M
backtrack(0)