import sys

N = int(input())
height = [int(sys.stdin.readline()) for _ in range(N)]

stk = []
ans = 0

for val in height:
    cur = [val, 1]

    while stk and stk[-1][0] <= val:
        ans += stk[-1][1]
        if val == stk[-1][0]:
            cur[1] += stk[-1][1]
        stk.pop()

    if stk:
        ans += 1
    stk.append(cur)

print(ans)