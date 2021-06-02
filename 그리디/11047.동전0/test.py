import sys
n,k=map(int,input().split())
arr=[int(input()) for _ in range(n)]
#print(arr)
result=0
for i in range(1,n+1):
    max=arr[-i] #max
    if max<=k:
        tmp=k//max
        k=k-(max*tmp)
        result=result+tmp
print(result)

'''
input
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
ouput
6
'''
