from sys import stdin

while True:
    sentence = stdin.readline().strip('\n')
    if sentence == ".": break

    balanced = True

    stack = []
    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()
    
    if stack: balanced = False
    print("yes" if balanced else "no")