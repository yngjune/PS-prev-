# Activity Selection Problem
from sys import stdin
from functools import cmp_to_key

def compare(i1, i2):
    if i1[1] == i2[1]:
        return i1[0] - i2[0]
    return i1[1] - i2[1]

N = int(input())
meeting = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
meeting.sort(key=cmp_to_key(compare))

ans = 0
last = 0
for m in meeting:
    if m[0] >= last:
        ans += 1
        last = m[1]
print(ans)