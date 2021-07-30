import sys
input=sys.stdin.readline
n=int(input())
arr=sorted(list(map(int,input().split())))
#비교대상
left1=0
right1=n-1
answer=arr[left1]+arr[right1]
#하나하나 검색해볼 대상
left2=left1
right2=right1
while left1<right1:
    tmp=arr[left1]+arr[right1]
    if abs(answer)>abs(tmp): #절대값이 작을수록 0에 가까움
        answer=tmp #더 작은값을 비교할 값으로 바꿈
        left2=left1
        right2=right1
        if answer==0: #아예0이 나오면
            break
    if tmp<0: #0보다작을때, 0에 가까워지려면 커져야함
        left1=left1+1
    else: #0보다 클때, 0에 가까워지려면 작아져야
        right1=right1-1
print(arr[left2],arr[right2])
