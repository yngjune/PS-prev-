def count_vowels():
    res = 0
    for c in seq:
        if c in "aeiou":
            res += 1
    return res


def backtrack(depth, start):
    if depth == L:
        num_vowels = count_vowels()
        num_cons = L - num_vowels

        if num_vowels < 1 or num_cons < 2:
            return

        print(*seq, sep='')
        return

    for i in range(start, C):
        seq[depth] = chars[i]
        backtrack(depth+1, i+1)


L, C = map(int, input().split())
chars = list(input().split())
chars.sort(key=lambda x:ord(x))
seq = ['0'] * L
backtrack(0, 0)