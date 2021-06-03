import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
qu=deque()
for i in range(1,n+1):
    qu.append(i)
print(qu)

result=[]
while len(qu)!=0:
    for _ in range(k):
        qu.append(qu.popleft())
    result.append(qu.pop())

print('<' + ', '.join(map(str,result)) + '>')
    #<3, 6, 2, 7, 5, 1, 4>
