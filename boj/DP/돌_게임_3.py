n = int(input())

dp = [True for _ in range(n+1)]
for i in range(n, 0, -1):
    if not dp[i]:
        continue

    for j in [i-1, i-3, i-4]:
        if j <= 0:
            break
        dp[j] = False

if n < 4:
    res = ["00", "SK", "CY", "SK"]
    print(res[n])
elif dp[1] or dp[3] or dp[4]:
    print("SK")
else:
    print("CY")