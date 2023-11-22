n = int(input())
ans = 0
row = [0 for _ in range(n)]
visit_ver = [False for _ in range(n)]
visit_rud = [False for _ in range(2*n)]
visit_lud = [False for _ in range(2*n)]


def proper(x, y):
    if not visit_ver[y] and not visit_rud[x+y] and not visit_lud[n+x-y]:
        return True
    return False


def backtrack(d):
    if d == n:
        global ans
        ans += 1
        return
    
    for i in range(n):
        row[d] = i
        if proper(d, i):
            visit_ver[i] = True
            visit_rud[d+i] = True
            visit_lud[n+d-i] = True
            backtrack(d+1)
            visit_ver[i] = False
            visit_rud[d+i] = False
            visit_lud[n+d-i] = False

backtrack(0)
print(ans)