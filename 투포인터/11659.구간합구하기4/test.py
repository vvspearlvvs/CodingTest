#수n개가 주어졌을때, i번째수부터 j번째 수까지 합구하기
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
data=list(map(int,input().split()))

#구간합 알고리즘 적용
sum_value=0 #부분합계산
prefix_sum=[0] #접두사합 배열

#접두사합 배열 계산
for i in data:
    sum_value+=i #부분합
    prefix_sum.append(sum_value) #부분합결과 미리 저장해둠
print(prefix_sum)

for _ in range(m):
    i,j=map(int,input().split())
    #i부터j까지 합
    print(prefix_sum[j]-prefix_sum[i-1])
