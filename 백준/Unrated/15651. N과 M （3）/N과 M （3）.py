def backtrack(depth):
    if depth == M:
        print(*sequence)
        return
    
    for i in range(1, N+1):
        sequence[depth] = i
        backtrack(depth + 1)

N, M = map(int, input().split())
sequence = [0] * M
backtrack(0)