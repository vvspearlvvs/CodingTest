
'''
#2839.구구단
n=int(input())
for i in range(9):
    result = n * (i+1)
    print('{} * {} = {}'.format(n,i+1,result))
'''
#10871.X보다작은수
import sys
input=sys.stdin.readline
n,x=map(int,input().split())
A=list(map(int,input().split()))
for a in A:
    if a<x:
        print(a,end=' ')
