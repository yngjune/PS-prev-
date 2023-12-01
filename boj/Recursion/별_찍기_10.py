n = int(input())
out = [[" " for _ in range(n)] for _ in range(n)]

def fill(x, y, n):
    if n == 3:
        out[x][y:y+3] = ["*", "*", "*"]
        out[x+1][y:y+3] = ["*", " ", "*"]
        out[x+2][y:y+3] = ["*", "*", "*"]
        return
    
    nn = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            fill(x+nn*i, y+nn*j, nn)

fill(0, 0, n)

for line in out:
    print(*line, sep="")