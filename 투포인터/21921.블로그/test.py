#시간초과
#결과를 만들어두고
#다시 그 안에서 max,count로 답이 되는걸 또 뽑아서?

import sys
input=sys.stdin.readline

N,X=map(int,input().split())
data=list(map(int,input().split()))

#구간합 알고리즘 변형
prefix_sum=[] #접두사합 배열

#접두사합 배열 계산 (X단위로 부분합저장)
for i in range(len(data)-X+1):
    sum_value=0
    print(data[i:i+X])
    sum_value=sum(data[i:i+X]) #부분합
    prefix_sum.append(sum_value) #부분합결과 미리 저장해둠

#print(prefix_sum)
max_ans=max(prefix_sum)
if max_ans == 0:
    print("SAD")
else:
    print(max_ans)
    print(prefix_sum.count(max_ans))
