def fill(num, r, c):
    if num == 1:
        return

    next = num // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                fill_blank(next, r+i*next, c+j*next)
            else:
                fill(next, r + next * i, c + next * j)


def fill_blank(num, r, c):
    for i in range(num):
        for j in range(num):
            arr[r+i][c+j] = ' '


N = int(input())
arr = [['*'] * N for _ in range(N)]
fill(N, 0, 0)


for i in range(N):
    for j in range(N):
        print(arr[i][j], end='')
    print()