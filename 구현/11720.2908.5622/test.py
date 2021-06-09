'''
#11720.숫자의합
import sys
input=sys.stdin.readline
n=input()
str=list(map(int,input().rstrip()) for _ in range(input()))
print(sum(str))
'''
'''
#2908.상수
str=list(map(int,input().split()))
max=0
for i in str:
    a=i//100
    b=(i%100)//10
    c=i%10
    new_str = c*100+b*10+a
    if max<new_str:
        max=new_str
print(max)
'''
'''
#5622.다이얼
dials=['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
str=input()
result=0
for dial in dials: #dial : ABC
    for d in dial: #d :A
        for i in str:
            if i == d:
                result = result+dials.index(dial)+1
print(result)
'''
