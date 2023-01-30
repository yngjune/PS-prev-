import sys

class Stack:
    def __init__(self) -> None:
        self.data = []

    def push(self, x) -> None:
        self.data.append(x)

    def pop(self):
        if self.empty():
            return -1
        return self.data.pop()

    def size(self) -> int:
        return len(self.data)

    def empty(self) -> int:
        if len(self.data) == 0:
            return 1
        return 0

    def top(self):
        if self.empty():
            return -1
        return self.data[len(self.data)-1]

stk = Stack()
T = int(input())
for _ in range(T):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stk.push(command[1])
    if command[0] == 'pop':
        print(stk.pop())
    if command[0] == 'size':
        print(stk.size())
    if command[0] == 'empty':
        print(stk.empty())
    if command[0] == 'top':
        print(stk.top())