from collections import deque
from sys import stdin

N, L = map(int, input().split())
arr = map(int, stdin.readline().split())

wnd = deque()

i = 0
for val in arr:
    while wnd and wnd[-1][0] > val:
        wnd.pop()
    while wnd and wnd[0][1] <= i - L:
        wnd.popleft()
    
    wnd.append((val,i))
    i += 1
    print(wnd[0][0], end=' ')