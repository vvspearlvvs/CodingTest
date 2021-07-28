#두 배열을 합친다음 정렬해서 출력
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
print(alist) #[3,5]
print(blist) #[2,9]
result=alist+blist
result.sort()
print(''.join(result))

'''
#포인터 이동하면서 최대한 합치기
l,r=0,0
result=[]
while l<r and r<m:
    if alist[l]<blist[r]:
        result.append(alist[l])
        l+=1 #다음 alist원소
    else:
        result.append(blist[r])
        r+=1 #다음 blist원소
print(result)

#남은 배열 합치기
while l<n:
    result.append(alist[l])
    l+=1
while r<m:
    result.append(blist[r])
    r+=1
print(' '.join(map(str,result)))
'''
