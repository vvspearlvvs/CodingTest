import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
#print(arr) #list [3,1,4,3,2]
line={i+1:arr[i] for i in range(len(arr))}
line=sorted(line.items(),key=lambda x:x[1])
print(line) #list [(2, 1), (5, 2), (1, 3), (4, 3), (3, 4)]

result=[]
tmp=0
for k,v in line:
    tmp=tmp+v
    result.append(tmp)
print(sum(result))
