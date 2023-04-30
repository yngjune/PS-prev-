N = int(input())
arr = [int(input()) for _ in range(N)]

ans = 0
for i in range(N-2, -1, -1):
    while arr[i] >= arr[i+1]:
        arr[i] -= 1
        ans += 1

print(ans)