from sys import stdin

arr = stdin.readline()[:-1]

score = 0
tmp = 1
stack = []
valid = True

for i in range(len(arr)):
    if arr[i] == '[':
        stack.append('[')
        tmp *= 3

    elif arr[i] == '(':
        stack.append('(')
        tmp *= 2

    elif arr[i] == ']':
        if not stack or stack[-1][0] != '[':
            valid = False
            break
        if arr[i-1] == '[':
            score += tmp
        tmp //= 3
        stack.pop()

    elif arr[i] == ')':
        if not stack or stack[-1][0] != '(':
            valid = False
            break
        if arr[i-1] == '(':
            score += tmp
        tmp //= 2
        stack.pop()
        


if stack:
    valid = False

print(score if valid else 0)