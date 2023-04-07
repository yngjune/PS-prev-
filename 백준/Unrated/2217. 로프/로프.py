from sys import stdin
N = int(input())
rope = [int(stdin.readline()) for _ in range(N)]
rope.sort(reverse=True)

max_weight = 0
for i in range(N):
    cur_weight = (i+1) * rope[i]
    if cur_weight > max_weight:
        max_weight = cur_weight

print(max_weight)