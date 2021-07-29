#i번째 수부터 j번째 수까지의 합
#A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우
#2018문제와 차이점은?

import sys
input=sys.stdin.readline

n,m=map(int,input().split())
data=list(map(int,input().split()))

subsum=0
end=0 #start와 end가 같이 시작
cnt=0
for start in range(n):
    while subsum<m and end<n: # 부분합이 n보다 작으면
        subsum+=data[end]
        end+=1
    if subsum==m: # 부분합이 N이 되면
        cnt+=1
    subsum-=data[start]
print(cnt)
