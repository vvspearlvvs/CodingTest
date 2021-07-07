'''
#10950.A+B-3
T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    print(a+b)

#15552.빠른 A+B
import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    print(a+b)

#11021. A+B-7
import sys
input=sys.stdin.readline
T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    print("Case #{}: {}".format(i+1,a+b))


#11022. A+B-7
import sys
input=sys.stdin.readline
T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    print("Case #{}: {} + {} = {}".format(i+1,a,b,a+b))
'''
#10953. A+B-6
import sys
input=sys.stdin.readline
T=int(input())
for i in range(T):
    a,b= map(int,input().split(","))
    print(a+b)
