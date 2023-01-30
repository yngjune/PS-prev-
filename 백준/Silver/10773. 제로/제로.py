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

    def empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False

    def top(self):
        if self.empty():
            return -1
        return self.data[len(self.data)-1]

stk = Stack()
T = int(input())
for _ in range(T):
    num = int(input())
    if num == 0:
        stk.pop()
    else:
        stk.push(num)

result = 0
while not stk.empty():
    result += stk.pop()

print(result)