import sys

N = int(input())
stk = []
nge = [-1] * N
nums = list(map(int, sys.stdin.readline().split()))

for i in range(N-1,-1,-1):
    while stk and stk[-1] <= nums[i]:
        stk.pop()
    if stk:
        nge[i] = stk[-1]
    stk.append(nums[i])

print(' '.join(map(str, nge)))