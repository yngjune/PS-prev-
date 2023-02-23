def equal(num, r, c):
    tmp = graph[r][c]
    for i in range(num):
        for j in range(num):
            if graph[r+i][c+j] != tmp:
                return False
    return True

def quad_tree(num, r, c):
    if num == 1:
        return str(graph[r][c])
    
    if equal(num, r, c):
        return str(graph[r][c])
    
    half = num >> 1
    return "(" + quad_tree(half, r, c) + quad_tree(half, r, c + half)\
        + quad_tree(half, r + half, c) + quad_tree(half, r + half, c + half) + ")"

    



N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
result = quad_tree(N, 0, 0)
print(result)