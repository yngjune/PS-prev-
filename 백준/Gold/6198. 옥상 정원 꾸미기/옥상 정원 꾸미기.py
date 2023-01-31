N = int(input())
MAX_HEIGHT = 1000000001

stk = []
heights = [0] * N
count = 0

for i in range(N):
    heights[i] = int(input())

stk.append((MAX_HEIGHT, N))

for i in range(N-1, -1, -1):
    while stk and stk[-1][0] < heights[i]:
        stk.pop()
    if stk:
        count += stk[-1][1] - i - 1
    stk.append((heights[i], i))

print(count)