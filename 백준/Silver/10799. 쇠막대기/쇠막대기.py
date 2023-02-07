from sys import stdin

sentence = stdin.readline()[:-1]
stack = []
first_pop = True
total = 0

for char in sentence:
    if char == '(':
        first_pop = True
        stack.append(char)
    else:
        stack.pop()
        if first_pop: # laser
            first_pop = False
            total += len(stack)
        else:
            total += 1
        
print(total)