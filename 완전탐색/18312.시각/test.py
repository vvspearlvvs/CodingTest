#문자열
n,k=map(int,input().split())
count=0
k=str(k)
for h in range(n+1):
    if h<10: h='0'+str(h)
    for m in range(60):
        if m<10: m='0'+str(m)
        for s in range(60):
            if s<10: s='0'+str(s)
            tmp="{}시 {}분 {}초".format(h,m,s)
            #print(tmp)
            if k in tmp: # 또는 if k in str(h)+str(m)+str(s):
                count=count+1
print(count)
