from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
com=[input().split() for _ in range(n)]
print(com)

queue=deque()

for c in com:
    if c[0] == 'push':
        queue.append(c[1])
    elif c[0] == 'pop':
        if len(queue) ==0:
            print(-1)
        else:
            print(queue.popleft())
    elif c[0] == 'size':
        print(len(queue))
    elif c[0] == 'empty':
        if len(queue) ==0:
            print(1)
        else:
            print(0)
    elif c[0] == 'back': #제일먼저들어온게 맨끝에
        if queue:
            print(-1)
        else:
            print(queue[-1])
    elif c[0] == 'front': #제일 나중에 들어온게 맨앞에
        if len(queue) ==0:
            print(-1)
        else:
            print(queue[0])
