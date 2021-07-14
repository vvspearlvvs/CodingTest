#luck잔고 초기값 : 0
#contest에서 이기면, luck잔고는 l[i]만큼 감소
#contest에서 지면, luck잔고는 l[i]만큼 증가
#T[i] contest의 중요도, 중요1 안중요0
#k번이상 중요한 contest에서 진다면, contest후에 luck잔고의 최대금액은?

#ex:k=2, L=5,1,4 T=1,2,0
#모든경기를 지면, 5+1+4=10

#luck를 최대로 모아야한다.
#즉, 최대한 contest에서 져야한다.
#안중요한 contest일때는(T=0) 무조건 지면 된다.
#중요한 contest일떄는(T=1) 행운이 큰 수 부터 진다.
#더이상 질 수 있는 횟수가 없어지면 이제 어쩔수 없이 이긴다.


def luckBalance(k, contests):
    luck=0
    #안중요한 contest부터 행운적립=계속 진다
    sort_contest=sorted(contests,key=lambda x:(x[1],-x[0]))
    #print(sort_contest)

    for scr in sort_contest:
        if scr[1] == 0: #안중요한 contests 무조건 진다
            luck+=scr[0]
        elif k>0:  # 이길수 있는 횟수가 남아있아있으면
            luck+=scr[0] #진다
            k-=1 #이길수 있는 횟수가 줄어듬
        else: #중요한 contest에서 어쩔수 없이 이긴다
            luck-=scr[0]
    return luck

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
contests = []
for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))
luckBalance(k, contests)
