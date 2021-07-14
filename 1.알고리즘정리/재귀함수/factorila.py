#반복구현
def fact(n):
    result=1
    for i in range(1,n+1):
        result+=i
    return result

#재귀구현
def fact2(n):
    if n<=1:
        return 1
    return n*fact2(n-1)

#최대공약수-재귀구현
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
