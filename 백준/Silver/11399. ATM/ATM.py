N = int(input())
arr = sorted(list(map(int, input().split())))
acc = [arr[0]] * N

ans = arr[0]
for i in range(1,N):
    acc[i] = acc[i-1] + arr[i]
    ans += acc[i]

print(sum(acc))