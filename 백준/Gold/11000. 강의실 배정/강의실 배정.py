import heapq
from sys import stdin

room = []

N = int(stdin.readline())
lec = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

lec.sort()
heapq.heappush(room, lec[0][1])

for i in range(1,N):
    cur = room[0]
    if lec[i][0] < cur:
        heapq.heappush(room, lec[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lec[i][1])

print(len(room))