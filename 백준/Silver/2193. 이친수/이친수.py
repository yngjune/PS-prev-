pinary = [0] * 100
pinary[1] = 1
pinary[2] = 1


N = int(input())
for i in range(3, N+1):
    pinary[i] = pinary[i-1] + pinary[i-2]
print(pinary[N])