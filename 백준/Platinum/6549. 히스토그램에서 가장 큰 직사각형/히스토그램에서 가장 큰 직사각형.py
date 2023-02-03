from sys import stdin

while True:
    nums = list(map(int, stdin.readline().split()))
    N = nums.pop(0)
    if N == 0: break

    stack = []
    area = 0

    for i in range(N):
        leftmost = i

        while stack and stack[-1][0] >= nums[i]:
            h, leftmost = stack.pop()
            area = max(area, h*(i-leftmost))

        stack.append([nums[i], leftmost])
    
    for h, l in stack:
        area = max(area, h*(N-l))
    print(area)