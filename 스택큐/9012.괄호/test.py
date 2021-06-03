import sys
input=sys.stdin.readline
T=int(input())
PS_list=[list(input()) for _ in range(T)]

def sol(PS):
    PS.pop()
    #print(PS)
    stack=[]
    for _ in range(len(PS)):
        tmp=PS.pop()
        if len(stack)==0:
            stack.append(tmp)
        else:
            if tmp=='('and stack[-1]==')':
                stack.pop()
            else:
                stack.append(tmp)
        #print(stack)
    if len(stack)==0:
        print("YES")
    else:
        print("NO")

for ps in PS_list:
    sol(ps)
