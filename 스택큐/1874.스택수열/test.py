#요구사항
#입력된 배열처럼 수열을 만드려면,
#어떻게 push(+),pop(-) 하나?
import sys
input=sys.stdin.readline

n=int(input())
stack=[]
result=[]
count=0
flag=True
for i in range(n):
    x=int(input())

    while count<x: #입력된 배열만큼 계속 append을 함
        count+=1
        stack.append(count)
        result.append("+")

    if stack[-1]==x: #젤 위에 있는 pop
        stack.pop()
        result.append("-")
    else: #불가능한경우
        flag=False
        break

if flag:
    print('\n'.join(result))
else: #불가능한경우
    print("NO")
