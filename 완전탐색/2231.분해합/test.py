n=int(input())
for i in range(1,n+1):
    arr=list(map(int,list(str(i))))
    if sum(arr)+i == n:
        print(i)
        break
    if i==n:
        print(0)
'''
#초안
n=int(input())
for i in range(1,n+1):
    a,b,c = i//100,(i%100)//10,(i%100)%10
    tmp_sum = i+a+b+c
    if tmp_sum == n:
        print(i)
        break
    if i==n:
        print(0)
'''
