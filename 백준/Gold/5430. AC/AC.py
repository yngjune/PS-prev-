from collections import deque
from sys import stdin

T = int(input())
for _ in range(T):
    cmd = stdin.readline()
    N = int(stdin.readline())
    try:
        d = deque(map(int,stdin.readline().strip("[]\n").split(',')))
    except:
        d = deque()
    is_error = False
    is_reverse = False

    for c in cmd:
        if c == 'R':
            is_reverse = not is_reverse
        if c == 'D':
            if len(d) == 0:
                is_error = True
                print("error")
                break
            else:
                if is_reverse:
                    d.pop()
                else:
                    d.popleft()
    
    if not is_error:
        if is_reverse:
            d.reverse()
        print('[',','.join(map(str,d)),']',sep='')