N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

count = [0, 0]

def equal(num, r, c):
    tmp = paper[r][c]
    for i in range(num):
        for j in range(num):
            if paper[r+i][c+j] != tmp:
                return False
    return True

def recur(num, r, c):
    if num == 1:
        count[paper[r][c]] += 1
        return

    # equals
    if equal(num, r, c):
        count[paper[r][c]] += 1
        return
    
    half = num // 2
    recur(half, r, c)
    recur(half, r, c + half)
    recur(half, r + half, c)
    recur(half, r + half, c + half)

recur(N, 0, 0)
print(count[0], count[1], sep='\n')