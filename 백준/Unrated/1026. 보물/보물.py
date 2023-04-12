N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

zipped = list(zip(range(N), B))
zipped.sort(key=lambda x:x[1], reverse=True)
A.sort()
shuffled = [0] * N

ans = 0
for i in range(N):
    shuffled[zipped[i][0]] = A[i]
for i in range(N):    
    ans += shuffled[i] * B[i]

print(ans)