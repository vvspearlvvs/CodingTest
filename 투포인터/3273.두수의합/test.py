import sys
input=sys.stdin.readline
n=int(input())

#정렬
arr=sorted(list(map(int,input().split())))
x=int(input())
print(arr)

left=0
right=n-1
#print(arr[left]+arr[right])
count=0

while left<right:
    if arr[left]+arr[right]==x:
        count=count+1
    if arr[left]+arr[right]<x:
        left=left+1
        continue #작은걸 계속 늘림
    right=right-1 #큰걸 계속 줄임
    print(left,right)

print(count)
