n = int(input().strip())
c = list(map(int, input().rstrip().split()))
global_index=len(c)-1
answer=0
check=0
while check<global_index: #전체리스트안에서
    #### indexError해결
    if check +2 <=global_index and c[check+2]==0: #2번점프 할 수 있을때
        check=check+2
        answer=answer+1
    elif c[check+1]==0: #1번점프 할 수 있을때
        check=check+1
        answer=answer+1
    print(check)
print(answer)
