n = int(input())
move = []

def hanoi(n, start, tmp, end):
    if n == 1:
        move.append((start, end))
    else:
        hanoi(n-1, start, end, tmp)
        move.append((start, end))
        hanoi(n-1, tmp, start, end)

hanoi(n, 1, 2, 3)
print(len(move))
for s, e in move:
    print(s, e)