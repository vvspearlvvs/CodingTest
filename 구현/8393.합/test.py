#893.합
n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#2741.n찍기
import sys
input=sys.stdin.readline
n=int(input())
for i in range(1,n+1):
    print(i)

#2742.기찍n
import sys
input=sys.stdin.readline
n=int(input())
for i in range(n,0,-1):
    print(i)
