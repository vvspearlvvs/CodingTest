#오른쪽으로 하나씩 이동, 마지막에 있는건 맨앞으로 이동
#n번 이동하고나서, 그 결과 리턴

def solution(A,K):
    if len(A) == K or len(A)==0: #예외사항 추가하기
        return A

    for i in range(K):
        tmp=A.pop(-1)
        A.insert(0,tmp)
    return A

A=[1,2,3,4]
K=3
print(solution(A,K))
