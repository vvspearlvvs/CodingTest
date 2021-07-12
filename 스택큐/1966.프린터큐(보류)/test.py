#요구사항
#중요도가 높은 순서대로 인쇄
#중요도가 높은문서가 하나라도 있으면,인쇄안하고 큐의 맨뒤로
#어떤 한 문서가 몇번쨰로 인쇄되는지 알아내시오

#첫번째 ㄱ밧이
import sys
from collections import deque
input = sys.stdin.readline

def sol(n,m,qu):
    #print(qu)
    idx=list(range(n)))
    index=[0 for _ in range(size)]
    index[m]=1 #찾으려고하는 문서의 현재위치->deque로도 가
    cnt=0
    while qu:
        if qu[0]==max(qu): #큐의 가장앞이 가장큰숫자인지 확인
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

T=int(input()) #테스트케이스 갯수
for _ in range(T):
    n,m=map(int,input().split()) #n:큐의 크기, m:찾을문서번
    qu=deque(map(int,input().split())) #중요도
    print(sol(n,m,qu))
