from sys import stdin

def rotate(gear, dir):
    result = [0] * 8
    if dir == 1:
        result[1:] = gear[:-1]
        result[0] = gear[-1]

    else:
        result[:-1] = gear[1:]
        result[-1] = gear[0]

    return result


def score(gears):
    result = 0
    tmp = 1
    for i in range(4):
        if gears[i][0] == '1':
            result += tmp
        tmp *= 2
    return result

gears = [list(stdin.readline().rstrip()) for _ in range(4)]
K = int(input())
for _ in range(K):
    gear_num, rot_dir = map(int, stdin.readline().split())
    gear_num -= 1
    rot_seq = [0] * 4
    rot_seq[gear_num] = rot_dir

    for i in range(gear_num-1, -1, -1):
        if gears[i][2] != gears[i+1][6]:
            rot_seq[i] = -rot_seq[i+1]
        else: break

    for i in range(gear_num+1, 4):
        if gears[i][6] != gears[i-1][2]:
            rot_seq[i] = -rot_seq[i-1]
        else: break

    for i in range(4):
        if rot_seq[i] == 0:
            continue
        gears[i] = rotate(gears[i], rot_seq[i])

print(score(gears))