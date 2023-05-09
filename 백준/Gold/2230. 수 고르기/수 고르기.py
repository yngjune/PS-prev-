from sys import stdin

N, M = map(int, input().split())
arr = [int(stdin.readline()) for _ in range(N)]
arr.sort()

ans = arr[-1] - arr[0]
l, r = 0, 0
while r < N:
    diff = arr[r] - arr[l]

    if diff < M:
        r += 1
    elif diff == M:
        ans = M
        break
    else:
        if diff < ans: ans = diff
        l += 1

print(ans)