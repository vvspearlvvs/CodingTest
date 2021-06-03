import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
qu=deque()
for i in range(1,n+1):
    qu.append(i)
#print(qu)

while len(qu)>1:
    qu.popleft()
    qu.append(qu.popleft())
#print(qu)
print(qu.pop())
