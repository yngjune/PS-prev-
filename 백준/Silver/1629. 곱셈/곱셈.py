A, B, C = map(int, input().split())

def pow(num, exp, mod):
    if exp == 1:
        return num % mod
    
    tmp = pow(num, exp//2, mod)
    if exp % 2 == 0:
        return (tmp * tmp) % mod
    else:
        return (tmp * tmp * num) % mod

print(pow(A, B, C))