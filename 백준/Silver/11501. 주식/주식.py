from sys import stdin

T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int, stdin.readline().split()))

    ans = 0
    cur_max = price[-1]
    for i in range(N-2, -1, -1):
        cur_max = price[i] if price[i] > cur_max else cur_max
        ans += cur_max - price[i]

    print(ans)