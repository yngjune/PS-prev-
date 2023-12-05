from sys import stdin

n = int(stdin.readline())
power = list(map(int, stdin.readline().split()))
power.sort()
ans = 0

for i in range(n-2):
    if power[i] > 0: break
    target = -power[i]
    left = i + 1
    right = n - 1

    while left < right:
        if power[left] + power[right] == target:
            if power[left] == power[right]:
                ans += (right - left + 1) * (right - left) // 2
                break
            else:
                ltmp, rtmp = power[left], power[right]
                lcnt, rcnt = 0, 0
                while power[left] == ltmp:
                    left += 1
                    lcnt += 1
                while power[right] == rtmp:
                    right -= 1
                    rcnt += 1
                ans += lcnt * rcnt
        elif power[left] + power[right] < target:
            left += 1
        else:
            right -= 1

print(ans)