N, K = map(int, input().split())

l = [i for i in range(1, N+1)]
cursor = N - 1
count = 0
ans = []

while count < N:
    for _ in range(K):
        cursor = (cursor + 1) % len(l)
    ans.append(str(l.pop(cursor)))
    cursor -= 1
    count += 1

print("<", ", ".join(ans), ">", sep='')