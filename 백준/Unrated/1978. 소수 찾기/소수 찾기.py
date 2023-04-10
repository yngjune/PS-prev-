MAX_NUM = 1000
is_prime = [True] * (1 + MAX_NUM)
is_prime[1] = False

for num in range(2, MAX_NUM+1):
    if not is_prime[num]: continue
    for next in range(num*2, MAX_NUM+1, num):
        is_prime[next] = False


N = int(input())
nums = list(map(int, input().split()))

ans = 0
for num in nums:
    if is_prime[num]:
        ans += 1
print(ans)