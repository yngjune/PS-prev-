from sys import stdin

def backtrack(depth, start, n):
    if depth == 6:
        print(*seq)
        return
    
    for i in range(start,n):
        seq[depth] = arr[i]
        backtrack(depth+1, i+1, n)

seq = [0] * 6
while True:
    arr = list(map(int, stdin.readline().split()))
    N = arr.pop(0)
    if N == 0: break
    backtrack(0, 0, N)
    print()