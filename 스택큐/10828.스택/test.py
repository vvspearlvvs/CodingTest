import sys
input=sys.stdin.readline
n=int(input())
com=[input().split() for _ in range(n)]
print(com)

stack=[]
for c in com:
    if c[0] == 'push':
        stack.append(c[1])
    elif c[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif c[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
