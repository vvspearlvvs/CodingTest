#mark가 가지고 있는 예산(k)안에서, 최대한 많은수의 toy구매
#toy가격이 리스트로 주어질때, mark가 살 수 있는 최대 toy수는?
def maximumToys(prices, k):
    prices.sort()
    print(prices)
    cnt=0
    for i in range(len(prices)):
        k=k-prices[i] #prices[i] toy를 사고, 남은 예산
        print(k)
        if k<0: #남은예산이 없을때
            break
        cnt=cnt+1 #살수있는개수
    return cnt


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
prices = list(map(int, input().rstrip().split()))
result = maximumToys(prices, k)
print(result)
