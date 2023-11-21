from sys import stdin

n = int(stdin.readline())
time = []
for _ in range(n):
    st, et = map(int, stdin.readline().split())
    time.append((et, st))
time.sort()

ans = 0
last = -1
for et, st in time:
    if st >= last:
        ans += 1
        last = et
print(ans)

# if sort is done by (st, et)
# sort(key=lambda x:(x[1], x[0]))