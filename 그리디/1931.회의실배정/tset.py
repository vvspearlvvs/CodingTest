n=int(input())
arr=[]

for _ in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))

arr.sort(key= lambda x:(x[1],x[0])) #끝나는 순서대로 정렬
print(arr)

count=1
end_time = arr[0][1]
for i in arr:
    if end_time<=i[0]:
        count=count+1
        end_time=i[1]
print(count)
