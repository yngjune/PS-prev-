a = input()
b = list(input())
b_len = len(b)

stk = []
for ch in a:
    stk.append(ch)
    if len(stk) < b_len:
        continue
    if stk[-b_len:] == b:
        for _ in range(b_len):
            stk.pop()

if not stk:
    print("FRULA")
else:
    print(*stk, sep='')