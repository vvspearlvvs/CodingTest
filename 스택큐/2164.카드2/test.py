#요구사항
#1번카드가 제일위에,N번카드가 제일 밑에
#제일위에 있는 카드를 버리고
#제일위에 있는카드를 제일아래로 옮긴다.
#카드가 한장남을때까지 반복한다
#마지막에 남게 되는 카드는?
import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
qu=deque()
for i in range(1,n+1):
    qu.append(i)
print(qu)

while len(qu)>1:
    qu.popleft()
    qu.append(qu.popleft())
#print(qu)
print(qu.pop())
