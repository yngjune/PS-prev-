def backtrack(depth, start):
    if depth == M:
        print(*sequence)
        return
    
    for i in range(start, N+1):
        sequence[depth] = i
        backtrack(depth + 1, i)

N, M = map(int, input().split())
sequence = [0] * M
backtrack(0, 1)