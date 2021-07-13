n=5 #데이터의 개수
m=5 #찾고자하는 부분합
data=[1,2,3,2,5] #전체수열

count=0
interval_sum=0
end=0
start=0

#start증가시키면서 반복
for start in range(n):

    #현재 부분합이 찾을 부분합(m)보다 작거나,
    #데이터의 범위를 벗어나지 않은 선에서 end가 오른쪽으로 이동
    while interval_sum<m and end<n:
        interval_sum+=data[end] #부분합증가
        end+=1

    #현재 부분합이 찾을 부분합(m)일때 count
    if interval_sum == m:
        count+=1
    #현재 부분합이 찾을 부분합(m)보다 크거나
    interval_sum-=data[start] #부분합감소
print(count)
