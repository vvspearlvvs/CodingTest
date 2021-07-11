#첫번째 값이 최대값이 될때 까지 첫번째깞을 맨뒤로 보냄
#첫번째 값이 최대값이 되면, order증가
#원래문서의 인덱스를 idx에 저장해두고,
#imp의 순서가 바뀔때마다 순서를 같이 바꿔준다.
#그래서 m번째 문서가 언제 출력되는지 리턴한다.

T=int(input()) #테스트케이스 갯수
for _ in range(T):
    n,m=map(int,input().split()) #n:큐의 크기, m:찾을문서번
    imp=list(map(int,input().split())) #중요도
    idx=list(range(len(imp)))
    #print(idx)
    idx[m]='target' #찾아야하는 문서
    order = 0 #순서

    for x in imp:
        if x==max(imp): #첫번째값이 최대값일경우
            order+=1
            if idx[0]=='target': #첫번째값이 내가 찾으려고 하는 문서일경우
                print(order)
                break
            else: #첫번쨰 값 제거
                imp.pop()
                idx.pop()
        else: #순서가 바뀔떄마다 계속 자리이동
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
        #print(imp)
        #print(idx)
