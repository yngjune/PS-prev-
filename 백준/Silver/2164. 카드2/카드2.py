from collections import deque

N = int(input())
deck = deque([i for i in range(1,N+1)])

for _ in range(N-1):
    deck.popleft()
    deck.append(deck.popleft())

print(deck[0])