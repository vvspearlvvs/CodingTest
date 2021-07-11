#요구사항
#입력으로 주어진 괄호문자열이 쌍이 맞는 올바른 괄호문자열인지 판단
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
