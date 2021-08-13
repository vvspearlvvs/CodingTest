#2원짜리동전, 5원짜리동전으로
#동전의 개수가 최소가 되도록 거슬러주기

#point : 최소를 위해 가장큰단위인 5로 나눔
#5로 못나누면 2원으로 거슬림
def test(n):
    count=0

    while n>0:
        if n%5==0:
            count+=n//5
            return count
        n-=2
        count+=1
    if n<0:
        return -1

n=int(input())
print(test(n))
