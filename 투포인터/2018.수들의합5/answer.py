# N을 몇 개의 연속된 자연수의 합으로 나타낼 수 있는지 그 가지수

n = int(input())
start,end = 0,1 #시작위치,끝위치
cnt = 0 #가지수
sum = 1 #부분합
while end<=n and start<=end:
    if sum < n: # 부분합이 n보다 작으면
        end+=1  # 오른쪽으로 이동
        sum+=end # 오른쪽값 부분합에 추가

    elif sum == n: # 부분합이 N이 되면
        cnt+=1 # 정답 가지수 Count
        end+=1 # 오른쪽으로 이동 (슬라이딩윈도우 맨끝위치)

        sum+=end #슬라이딩윈도우 맨뒤 추가
        sum-=start #슬라이딩윈도우 맨앞 빼기

        start+=1 #왼쪽이동 (슬라이딩윈도우 맨앞위치)

    else: #부분합보다 크면
        sum-=start #슬라이딩 윈도우  앞에 있는 숫자를 하나 뺌
        start+=1 #왼쪽이동 (슬라이딩윈도우 맨앞위치)
print(cnt)
