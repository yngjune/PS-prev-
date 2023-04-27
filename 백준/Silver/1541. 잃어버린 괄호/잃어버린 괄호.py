eqns = input().split('-')
nums = []

for eqn in eqns:
    cur = 0
    for ch in eqn.split('+'):
        cur += int(ch)
    nums.append(cur)

ans = nums[0]
for val in nums[1:]:
    ans -= val

print(ans)
