#요구사항
#중요도가 높은 순서대로 인쇄
#중요도가 높은문서가 하나라도 있으면,인쇄안하고 큐의 맨뒤로
#어떤 한 문서가 몇번쨰로 인쇄되는지 알아내시오

import sys
from collections import deque
input = sys.stdin.readline
T=int(input())

def sol(size,i,qu):
    #print(qu)
    index=[0 for _ in range(size)]
    index[i]=1 #찾으려고하는 문서의 현재위치->deque로도 가#
    cnt=0
    while qu:
        if qu[0]==max(qu):
            if index[0]==1:
                break
            else:
                qu.popleft()
                index.pop(0)
                cnt=cnt+1
        else:
            qu.append(qu.popleft())
            index.append(index.pop(0))
            #print(index)
    return cnt+1

for i in range(T):
    size,i=map(int,input().split())
    qu=deque(map(int,input().split()))
    print(sol(size,i,qu))
