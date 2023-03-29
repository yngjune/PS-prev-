from sys import stdin

def rotate_step(dir):
    if dir == (0, 1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, -1)
    elif dir == (0, -1):
        return (-1, 0)
    else:
        return (0, 1)


def rotate_dir(dir, state):
    for k in range(state):
        dir = rotate_step(dir)
    return dir


def is_cctv(num):
    return True if 1 <= num <= 5 else False


def eval(seq):
    seq_idx = 0
    # reset office
    for i in range(N):
        for j in range(M):
            if office[i][j] == -1:
                office[i][j] = 0

    # evaluate
    for i in range(N):
        for j in range(M):
            if is_cctv(office[i][j]):
                cur_state = seq[seq_idx]
                cctv_num = office[i][j]
                seq_idx += 1

                for dir in cctv_dir[cur_state][cctv_num]:
                    ni, nj = i, j
                    while True:
                        ni += dir[0]
                        nj += dir[1]
                        if ni < 0 or ni >= N or nj < 0 or nj >= M:
                            break
                        if is_cctv(office[ni][nj]):
                            continue
                        if office[ni][nj] == 6:
                            break
                        office[ni][nj] = -1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if office[i][j] == 0: cnt += 1
    return cnt


def backtrack(depth):
    if depth == num_cctv:
        global ans
        ans = min(ans, eval(state_seq))
        return
    
    for i in range(4):
        state_seq[depth] = i
        backtrack(depth+1)


# cctv_dir[i][j] = direction list for state #i, cctv #j
cctv_dir = [
    [ # state 0
        [],
        [(0, 1)], # cctv 1
        [(0, -1), (0, 1)], # cctv 2
        [(-1, 0), (0, 1)], # cctv 3
        [(0, -1), (-1, 0), (0, 1)], # cctv 4
        [(0, -1), (-1, 0), (0, 1), (1, 0)] # cctv 5
    ]
]

# cctv directions for each state (0~3)
for state in range(1, 4):
    tmp = [[]]
    for cctv in range(1,6):
        tmp2 = []
        for dir in cctv_dir[0][cctv]:
            next_dir = rotate_dir(dir, state)
            tmp2.append(next_dir)
        tmp.append(tmp2)

    cctv_dir.append(tmp)

    

N, M = map(int, input().split())
office = [list(map(int, stdin.readline().split())) for _ in range(N)]
num_cctv = 0
ans = N * M

for i in range(N):
    for j in range(M):
        if is_cctv(office[i][j]):
            num_cctv += 1

state_seq = [0] * num_cctv
backtrack(0)
print(ans)