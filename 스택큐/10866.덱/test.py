from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
com=[input().split() for _ in range(n)]
print(com)

qu=deque()

for c in com:
    if c[0] == 'push_front':
        qu.appendleft(c[1])
    elif c[0] == 'push_back':
        qu.append(c[1])
    elif c[0] == 'pop_front':
        if len(qu) ==0:
            print(-1)
        else:
            print(qu.popleft())
    elif c[0] == 'pop_back':
        if len(qu) ==0:
            print(-1)
        else:
            print(qu.pop())
    elif c[0] == 'size':
        print(len(qu))
    elif c[0] == 'empty':
        if len(qu) ==0:
            print(1)
        else:
            print(0)
    elif c[0] == 'back': #제일먼저들어온게 맨끝에
        if len(qu) ==0:
            print(-1)
        else:
            print(qu[-1])
    elif c[0] == 'front': #제일 나중에 들어온게 맨앞에
        if len(qu) ==0:
            print(-1)
        else:
            print(qu[0])
