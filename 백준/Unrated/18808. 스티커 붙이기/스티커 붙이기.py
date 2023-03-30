from sys import stdin

def rotate_sticker(sticker, row, col):
    rotated = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            rotated[j][row-i-1] = sticker[i][j]
    return rotated


def count_attached(graph, row, col):
    ans = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1: ans += 1
    return ans


def check_duplicate(laptop,sticker,x,y,r,c):
    for i in range(r):
        for j in range(c):
            if sticker[i][j] and laptop[x+i][y+j]:
                return True
    
    return False


def find_pos(laptop, sticker, n, m, r, c):
    for i in range(n):
        for j in range(m):
            if i + r - 1 >= n or j + c - 1 >= m:
                continue
            if not check_duplicate(laptop, sticker, i,j,r,c):
                return (i, j)
    
    return (-1, -1)


def fill(laptop,sticker,x,y,r,c):
    for i in range(r):
        for j in range(c):
            if sticker[i][j]:
                laptop[x+i][y+j] = 1


N, M, K = map(int, input().split())
laptop = [[0] * M for _ in range(N)]
for _ in range(K):
    R, C = map(int, stdin.readline().split())
    sticker = [list(map(int, stdin.readline().split())) for _ in range(R)]

    for i in range(4):
        x, y = find_pos(laptop, sticker, N, M, R, C)
        if (x,y) == (-1, -1):
            sticker = rotate_sticker(sticker, R, C)
            R, C = len(sticker), len(sticker[0])
            continue
        fill(laptop, sticker, x, y, R, C)
        break


print(count_attached(laptop, N, M))