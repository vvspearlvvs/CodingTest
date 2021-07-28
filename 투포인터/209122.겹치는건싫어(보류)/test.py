import sys
input=sys.stdin.readline

N,K=map(int,input().split())
data=list(map(int,input().split()))

result=[]
for i in range(len(data)):
    result.append(data[i])
    if result.count(data[i])>K:
        break
        #value,max_count=data[i],result.count(data[i])
        #print(value,max_count)
    answer=result
print(len(answer))

참고 https://develoger.kr/20922%EB%B2%88-%EA%B2%B9%EC%B9%98%EB%8A%94%EA%B1%B4-%EC%8B%AB%EC%96%B4/
