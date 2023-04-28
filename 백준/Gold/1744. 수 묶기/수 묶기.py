N = int(input())
ans = 0
pos = []
neg = []

def pair_sum(arr):
    idx = len(arr) - 1
    ret = 0
    while idx > 0:
        ret += arr[idx] * arr[idx-1]
        idx -= 2
    
    if idx == 0: ret += arr[0]
    return ret

for i in range(N):
    tmp = int(input())
    if tmp == 1: 
        ans += 1
    elif tmp > 0:
        pos.append(tmp)
    else:
        neg.append(tmp)
    
pos.sort()
neg.sort(reverse=True)
ans += pair_sum(pos) + pair_sum(neg)
print(ans)