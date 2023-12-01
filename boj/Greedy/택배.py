from sys import stdin

n, capacity = map(int, stdin.readline().split())
m = int(stdin.readline())
order = []
load = [0 for _ in range(n+1)]

for _ in range(m):
    snd, rcv, box = map(int, stdin.readline().split())
    order.append((snd,rcv,box))

order.sort(key=lambda x:(x[1],x[0]))

ans = 0
for f, t, b in order:
    loadable = True
    for i in range(f, t):
        b = min(b, capacity - load[i])
        if b == 0:
            loadable = False
            break
    if loadable:
        ans += b
        for i in range(f, t):
            load[i] += b

print(ans)