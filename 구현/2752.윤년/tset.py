'''
#2752.윤년
n=int(input())
if n%4==0 and n%100!=0 or n%400==0:
    print(1)
else:
    print(0)
'''
'''
#1212.8진수->2진수
n=input()
ten=int(n,8) #N진수->10진수 : int(n,N)
two=bin(ten) #10진수->2진수 : bin()
print(two[2::])
'''
#20053.최소,최대2
T=int(input())
for _ in range(T):
    n=int(input())
    alist=list(map(int,input().split()))
    print(min(alist),max(alist))
