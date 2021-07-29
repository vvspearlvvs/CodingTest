#바로 답을 찾을 수 있도록 변경
#슬라이딩 윈도우 방법 출처 https://welog.tistory.com/317

import sys
input=sys.stdin.readline

N,X=map(int,input().split())
data=list(map(int,input().split()))

if max(data) == 0:
    print("SAD")
else:
    #print("split",data[:X])
    value = sum(data[:X]) #X개씩 나눠서 sum
    #print("sum",value)

    max_value=value
    max_cnt=1

    for i in range(X,N):
        value+=data[i] #슬라이딩윈도우 앞에
        #print("+",data[i],"value",value)
        value-=data[i-X] #슬라이딩윈도우 뒤에값
        #print("-",data[i-X],"value",value)
        #print("최종",value)
        if value > max_value:
            max_value=value
            max_cnt=1
        elif value == max_value:
            max_cnt+=1
    print(max_value)
    print(max_cnt)
