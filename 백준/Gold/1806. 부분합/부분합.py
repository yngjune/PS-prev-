N, S = map(int, input().split())
arr = list(map(int, input().split()))
left, right, cur_sum, ans = 0, 0, 0, 0x7fff_ffff

while left <= right:
    if cur_sum >= S:
        ans = min(ans, right - left)
        cur_sum -= arr[left]
        left += 1
    elif right == N: break
    else:
        cur_sum += arr[right]
        right += 1

if ans == 0x7fff_ffff:
    print(0)
else:
    print(ans)