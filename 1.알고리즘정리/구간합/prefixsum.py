n=5 #데이터개수
data=[10,20,30,40,50] #데이터

sum_value=0 #부분합계산
prefix_sum=[0] #접두사합 배열

#접두사합 배열 계산
for i in data:
    sum_value+=i #부분합
    prefix_sum.append(sum_value) #부분합결과 미리 저장해둠

#left부터 right까지 구간합을 구하시오
left=3
right=4
print(prefix_sum[right]-prefix_sum[left-1])
