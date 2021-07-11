def pickingNumbers(a):
    result=[]
    a.sort()
    max=len(result)
    for i in range(len(a)):
        result.append(a[i])
        tmp=a[i+1::]
        for k in range(len(tmp)):
            if abs(a[i]-tmp[k])<=1:
                result.append(tmp[k])
        if max<len(result):
            max=len(result)
        #print(result)
        result=[]
    return max
n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)
print(result)
