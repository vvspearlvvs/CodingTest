import sys
input=sys.stdin.readline
n,s=map(int,input().split())
arr=sorted(list(map(int,input().split())),reverse=True)
#print(arr) #애초에 큰수부터 정렬해두면 더 빨리찾음->하지만 시간초과
start=0
end=start+1
sub_arr=arr[start:end+1] #start부터end까지 합
#print(sub_arr)
subsum=sum(sub_arr)
result=n+1 #최소의 길이를 구해야되서 최대값으로 초기
while start<end:
    #print(start,end)
    if subsum>=s:
        start=start+1
        end=end+1 #s보다 크면 둘다 투포인터 앞으로
        len=end-start+1
        if result>len: #길이(len(sub_arr))가 최소일때
            result=len
    elif subsum<s:
        end=end+1 #s보다 작으면 end만 앞으로가서 길이늘림
        if end>=n: #무한대로 늘리는게 아니라 수열 끝까지
            break
    sub_arr=arr[start:end+1] #포인터변경한걸로 새로운 부분합
    #print(sub_arr)
    subsum=sum(sub_arr)
    #print(start,end)
if result == n+1:
    print(0)
else:
    print(result)
