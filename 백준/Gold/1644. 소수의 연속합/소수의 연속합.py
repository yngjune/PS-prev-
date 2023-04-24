MAX_N = 4000000

sieve = [True] * (MAX_N+1)
primes = []
for i in range(2, MAX_N+1):
    if not sieve[i]: continue
    primes.append(i)
    for j in range(i*2, MAX_N+1, i):
        sieve[j] = False


N = int(input())
left, right, cur_sum, ans = 0, 1, primes[0], 0
while True:
    if cur_sum > N:
        cur_sum -= primes[left]
        left += 1

    elif cur_sum < N:
        if right == len(primes): break
        cur_sum += primes[right]
        right += 1

    else:
        ans += 1
        if right == len(primes): break
        cur_sum += primes[right]
        right += 1


print(ans)