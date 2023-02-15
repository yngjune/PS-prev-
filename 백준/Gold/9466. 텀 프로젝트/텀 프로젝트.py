from sys import stdin

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, stdin.readline().split()))
    visit = [False] * (N + 1)
    result = 0
    
    for i in range(1, N+1):
        path = []
        cur = i

        while not visit[cur]:
            visit[cur] = True
            path.append(cur)
            cur = arr[cur]
    
        if cur in path:
            result += len(path) - path.index(cur)

    print(N - result)