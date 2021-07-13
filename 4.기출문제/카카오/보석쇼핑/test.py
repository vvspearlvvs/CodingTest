#3테스트케이스를 통과하지 못했다

def solution(gems):
    group=set(gems)
    n=len(group) #종류의 수
    #print("종류",group) #종류
    #print("종류의수",n)
    answer=[]
    min=10000
    for i in range(len(gems)-n+1): #종류의 수보다 작으면 안셈
        for k in range(i+n,len(gems)):
            tmp=gems[i:k]
            print(tmp)
            if set(tmp)==set(group):
                #print("모든종류")
                if len(tmp) < min:
                    min=len(tmp)
                    print("가장짧은길이",min)

                    answer=[]
                    answer.append(i+1)
                    answer.append(k)
            else:
                print("종류가 하나라도 없음")
    return answer


gems =["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
res=solution(gems)
print("######")
print(res)
gems2=["AA", "AB", "AC", "AA", "AC"]
res=solution(gems2)
print("######")
print(res)
gems3=["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
res=solution(gems3)
print("######")
print(res)
