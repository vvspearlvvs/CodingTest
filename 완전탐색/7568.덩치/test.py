n=int(input())
arr=[]
for _ in range(n):
    (k,v)=map(int,input().split())
    arr.append((k,v))
print(arr)

for item in arr:
    result=1
    for item2 in arr:
        if item[0]<item2[0] and item[1]<item2[1]:
            result = result+1
    print(result,end=' ')
