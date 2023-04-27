from sys import stdin

def md_to_int(m, d):
    return m * 100 + d

N = int(input())
flower = []
for i in range(N):
    sm, sd, em, ed = map(int, stdin.readline().split())
    flower.append((md_to_int(sm, sd), md_to_int(em, ed)))
flower.sort(key=lambda x:(x[0], x[1]))

cur_date = 301
last_date = 1201
ans = 0

while cur_date < last_date:
    next_date = cur_date
    
    for i in range(N):
        start, end = flower[i]
        if start <= cur_date and end > next_date:
            next_date = end

    if next_date == cur_date:
        ans = 0
        break

    ans += 1
    cur_date = next_date

print(ans)