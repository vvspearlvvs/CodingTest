#for만 사용 : 메모리 29200KB, 시간168mx
n,m=map(int,input().split())
arr=list(map(int,input().split()))
MAX=0


for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for z in range(j+1,len(arr)):
            if arr[i]+arr[j]+arr[z]<=m:
                MAX=max(MAX,arr[i]+arr[j]+arr[z])
print(MAX)
