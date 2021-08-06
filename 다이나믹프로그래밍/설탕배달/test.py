#3킬로봉지, 5킬로봉지
#최대한 봉지의 수를 적게만들면서, n킬로 배달
n=int(input())
bag=0

while n>=0:
    if n%5==0:
        bag+=(n//5)
        print(bag)
        break
    n-=3 #5의배수가 될때까지 설탕-3, 봉지+1
    bag+=1
else:
    print(-1)
