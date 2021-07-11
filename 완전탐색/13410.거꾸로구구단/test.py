m,n=map(int,input().split())
multi=[]
for i in range(1,n+1):
    multi.append(str(m*i))
print(multi)

result=[]
for m in multi:
    result.append(int(m[::-1]))
print(max(result))
