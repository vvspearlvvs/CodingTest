import sys
input = sys.stdin.readline

#n:데이터의 개수, m:변경횟수, k:구간합계산 횟수
n,m,k=map(int,input().split())

arr=[0]*(n+1)
tree=[0]*(n+1)

#i번쨰까지 누적합을 계산하는 함수
def prefix_sum(i):
    result=0
    while i>0:
        result+=tree[i]
        #0이 아닌 마지막 비트만큼 빼가면서 이동
        i-=(i&-i)
    return result

#i번쨰 수를 dif만큼 더하는 함수
def update(i,dif):
    while i<=n:
        tree[i]+=dif
        i+=(i&-i)

#strt부터end까지 구간합계산하는 함수
def interval_sum(start,end):
    return prefix_sum(end)-prefix_sum(start-1)

#최종결과확인
for i in range(1,n+1):
    x=int(input())
    arr[i]=x
    update(i,x)

for i in range(m+k):
    a,b,c=map(int,input().split())
    #update연산일 경우
    if a==1:
        update(b,c-arr[b]) #바뀐크기(dif)만큼 적용
        arr[b]=c
    #구간합 연산일 경우
    else:
        print(interval_sum(b,c))
