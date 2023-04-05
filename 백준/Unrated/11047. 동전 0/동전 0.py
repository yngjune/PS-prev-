from sys import stdin

N, K = map(int, stdin.readline().split())
coin = list(map(int, [stdin.readline() for _ in range(N)]))

ans = 0
idx = len(coin) - 1
while K:
    q, K = divmod(K, coin[idx])
    ans += q
    idx -= 1
print(ans)