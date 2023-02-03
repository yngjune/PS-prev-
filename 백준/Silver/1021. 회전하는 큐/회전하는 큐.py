from collections import deque
from sys import stdin

N, M = map(int, input().split())
nums = list(map(int, stdin.readline().split()))

d = deque([i for i in range(1,N+1)])
min_cnt = 0

for target in nums:
    cnt = 0
    while d[0] != target:
        d.append(d.popleft())
        cnt += 1
    
    min_cnt += min(cnt, len(d)-cnt)
    d.popleft()

print(min_cnt)