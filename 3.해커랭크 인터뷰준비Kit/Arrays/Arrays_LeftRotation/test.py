#n:리스트길이
#m:반복할횟수
#리스트를 m번 왼쪽으로 이동시켰을때 결과는?
#1234 ->23451 -> 34512 -> 45123->51234
from collections import deque
def rotLeft(a,d):
    for _ in range(d):
        pop=a.popleft()
        a.append(pop)
        #print(dq)
    for _ in range(len(a)):
        print(a.popleft(),end=' ')

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
dq = deque(map(int, input().rstrip().split()))

rotLeft(dq,m)
