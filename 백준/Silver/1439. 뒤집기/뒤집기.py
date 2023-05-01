seq = input()
zero = 0
one = 0

idx = 0
while idx < len(seq):
    cur = seq[idx]
    if cur == '0': zero += 1
    elif cur == '1': one += 1

    while idx < len(seq) and seq[idx] == cur: idx += 1

print(min(zero, one))