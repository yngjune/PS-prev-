from collections import deque
from sys import stdin

d = deque()

N = int(input())
for _ in range(N):
    cmd = stdin.readline().split()

    if cmd[0] == "push":
        d.append(int(cmd[1]))

    elif cmd[0] == "pop":
        print(d.popleft() if len(d) else -1)

    elif cmd[0] == "size":
        print(len(d))

    elif cmd[0] == "empty":
        print(1 if not len(d) else 0)

    elif cmd[0] == "front":
        print(d[0] if len(d) else -1)

    elif cmd[0] == "back":
        print(d[-1] if len(d) else -1)