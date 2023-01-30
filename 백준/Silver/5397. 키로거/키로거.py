import sys

T = int(input())
for _ in range(T):
    text_list = []
    buf = []

    text = sys.stdin.readline().strip()
    for ch in text:
        if ch == '<':
            if len(text_list):
                buf.append(text_list.pop())
        elif ch == '>':
            if len(buf):
                text_list.append(buf.pop())
            pass
        elif ch == '-':
            if len(text_list):
                text_list.pop()
        else:
            text_list.append(ch)

    while len(buf):
        text_list.append(buf.pop())
    
    print(''.join(text_list))