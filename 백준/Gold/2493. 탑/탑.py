import sys

N = int(input())
stk = []
recv = [0] * N

nums = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    while len(stk) != 0 and stk[-1][0] < nums[i]:
        stk.pop()
    if len(stk) == 0:
        recv[i] = 0
    else:
        recv[i] = stk[-1][1] + 1
    stk.append((nums[i], i))

print(' '.join(map(str, recv)))