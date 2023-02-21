N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
count = [0, 0, 0] # 0, 1, -1

def equals(num, r, c):
    elem = paper[r][c]

    for i in range(num):
        for j in range(num):
            if paper[r+i][c+j] != elem:
                return False
    
    return True

def recur(num, r, c):
    if num == 1:
        count[paper[r][c]] += 1
        return

    div = num // 3
    # all number equals
    if equals(num, r, c):
        count[paper[r][c]] += 1
        return

    # else
    recur(num // 3, r, c)
    recur(num // 3, r, c+div)
    recur(num // 3, r, c+div*2)
    recur(num // 3, r+div, c)
    recur(num // 3, r+div, c+div)
    recur(num // 3, r+div, c+div*2)
    recur(num // 3, r+div*2, c)
    recur(num // 3, r+div*2, c+div)
    recur(num // 3, r+div*2, c+div*2)

recur(N, 0, 0)
print(count[-1], count[0], count[1], sep='\n')