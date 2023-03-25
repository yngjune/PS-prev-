def backtrack(depth, start):
    if depth == M:
        print(*seq)
        return
    
    prev = 0
    for i in range(start,N):
        if prev == arr[i]:
            continue
        prev = arr[i]
        seq[depth] = arr[i]
        backtrack(depth+1,i)
        

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
seq = [0] * M
backtrack(0, 0)