N = int(input())
cur = 1
stk = []
ops = []

for _ in range(N):
    tmp = int(input())
    while cur <= tmp:
        stk.append(cur)
        ops.append("+")
        cur += 1
    
    if stk[-1] != tmp:
        print("NO")
        break
    else:
        stk.pop()
        ops.append("-")

else:
    print("\n".join(ops))