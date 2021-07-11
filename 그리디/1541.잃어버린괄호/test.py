arr=input().split('-')
result=0
for i in arr[0].split('+'):
    result=result+int(i)
for i in arr[1::]:
    for j in i.split('+'):
        result=result-int(j)
print(result)

#-가 나올때까지 다 더하고, 그렇지 않으면 뺀다.
