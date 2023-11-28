from sys import stdin

MAXSIZE = 1000000001
MINSIZE = -1000000001
gmax = MINSIZE
gmin = MAXSIZE

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
opdb = list(map(int, stdin.readline().split()))
op = [-1 for _ in range(n-1)]

def binop(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        return int(a/b)

def calculate():
    tmp = num[0]
    for i in range(n-1):
        tmp = binop(tmp, num[i+1], op[i])

    return tmp

def backtrack(depth):
    if depth == n-1:
        cur = calculate()
        global gmin, gmax
        if gmin > cur:
            gmin = cur
        if gmax < cur:
            gmax = cur
        return
    
    for i in range(4):
        if opdb[i] > 0:
            opdb[i] -= 1
            op[depth] = i
            backtrack(depth+1)
            opdb[i] += 1

backtrack(0)
print(gmax)
print(gmin)