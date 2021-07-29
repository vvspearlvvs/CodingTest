# N을 몇 개의 연속된 자연수의 합으로 나타낼 수 있는지 그 가지수

#메모리초과 -> 직접 arr를 지정해서그런듯?
n=int(input())
arr=[i for i in range(1,n+1)]
print(arr)

end=0
subsum=0
ans=0
for start in range(n):
    while end<n and subsum<n: #슬라이딩윈도우 합이 N이 될때까지
        subsum+=arr[end] #하나씩 추가해서 합계산
        end+=1 #슬라이딩윈도우 앞으로 이동
    if subsum==n: #그러다가 합이 n이 되면
        ans+=1 #결과+1
    subsum-=arr[start] #슬라이딩윈도우 맨뒤에꺼 뺌
print(ans)
