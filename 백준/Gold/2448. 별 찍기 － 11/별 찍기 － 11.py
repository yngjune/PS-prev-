def star(num):
    if num == 3:
        return ["  *  ", " * * ", "*****"]
    
    prev = star(num//2)
    blank = " " * (num // 2)
    ans = []

    for line in prev:
        ans.append(blank + line + blank)
    for line in prev:
        ans.append(line + " " + line)

    return ans

N = int(input())
ans = star(N)

print(*ans, sep='\n')