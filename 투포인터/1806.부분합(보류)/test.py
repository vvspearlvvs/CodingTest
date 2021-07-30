import sys
input=sys.stdin.readline
n,s=map(int,input().split())
arr=list(map(int,input().split()))
#print(arr) #정렬없이 한다면..? -> 배열slice를 못함

start=0
end=start+1
subsum=arr[start]+arr[end] #start부터end까지 합
#print(sub_arr)
result=n+1 #최소의 길이를 구해야되서 최대값으로 초기화

while start<=end:
    #print(start,end)
    if subsum>=s:
        len=end-start+1
        if result>len: #길이가 최소일때
            result=len
        subsum=subsum-arr[start] #s보다 크면 맨앞 값을 뺌
        start=start+1 #end만 앞으로 감
    elif subsum<s:
        end=end+1 #s보다 작으면 end만 앞으로가서 길이늘림
        subsum=subsum+arr[end] #늘린만큼 subsum
        if end>=n: #무한대로 늘리는게 아니라 수열 끝까지
            break
if result == n+1:
    print(0)
else:
    print(result)
