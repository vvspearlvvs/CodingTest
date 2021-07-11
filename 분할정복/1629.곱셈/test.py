import sys
input=sys.stdin.readline
a,b,c = map(int,input().split())

def sol(a,b):
    if b==1:
        return a%c
    else:
        tmp=sol(a,b//2)
        if b%2==0:
            return (tmp*tmp)%c
        else:
            return (tmp*tmp*a)%c

print(sol(a,b))
