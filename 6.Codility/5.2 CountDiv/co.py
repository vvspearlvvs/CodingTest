#A와B사이의 숫자 리턴
#A<i<B , i mod K=0
#6 7 8 9 10 11 k=2 2로 나누어지는 숫자 : 6,8,10

#시간복잡도 B-A
def solution(A,B,K):
    cnt=0
    for i in range(A,B+1):
        if i%K ==0:
            cnt+=1
    return cnt

print(solution(6,11,2))
