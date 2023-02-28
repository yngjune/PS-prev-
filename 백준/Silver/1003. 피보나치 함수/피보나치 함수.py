fibo = [(0,0) for _ in range(41)]
fibo[0] = (1,0)
fibo[1] = (0,1)

for i in range(2, 41):
    zero = fibo[i-1][0] + fibo[i-2][0]
    one = fibo[i-1][1] + fibo[i-2][1]
    fibo[i] = (zero, one)

T = int(input())
for _ in range(T):
    N = int(input())
    print(*fibo[N])