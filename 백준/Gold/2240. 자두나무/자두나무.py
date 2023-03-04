from sys import stdin

def pos(cnt):
    return 1 + cnt % 2

T, W = map(int, input().split())
a = [0] + [int(stdin.readline()) for _ in range(T)]
d = [[0]*(W+1) for _ in range(T+1)]

# case w=0
for t in range(1,T+1):
    d[t][0] = d[t-1][0] + (1 if a[t] == 1 else 0)

# case 1<=w<=W
for t in range(1,T+1):
    for w in range(1,W+1):
        d[t][w] = max(d[t-1][w], d[t-1][w-1]) + (1 if a[t] == pos(w) else 0)

print(max(d[t]))