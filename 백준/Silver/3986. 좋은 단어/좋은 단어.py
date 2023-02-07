from sys import stdin

N = int(input())
cnt = 0

for _ in range(N):
    word = stdin.readline()[:-1]
    stack = []

    for char in word:
        if not stack:
            stack.append(char)
        else:
            if stack[-1] == char: stack.pop()
            else: stack.append(char)
    
    if not stack: cnt += 1

print(cnt)