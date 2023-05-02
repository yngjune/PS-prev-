import heapq
from sys import stdin

N, M = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
nums.sort()

for _ in range(M):
    c1 = heapq.heappop(nums)
    c2 = heapq.heappop(nums)
    heapq.heappush(nums, c1+c2)
    heapq.heappush(nums, c1+c2)

print(sum(nums))