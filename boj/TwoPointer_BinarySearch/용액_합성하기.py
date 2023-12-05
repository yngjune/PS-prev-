from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

l, r = 0, n-1
ans = arr[l] + arr[r]

while l < r:
    cur = arr[l] + arr[r]
    if abs(ans) > abs(cur):
        ans = cur

    if cur == 0:
        ans = 0
        break
    elif cur < 0:
        l += 1
    else:
        r -= 1

print(ans)