#홀수를 가지고 있는 배열
#같은 값을 가지고 있는 짝이 된다.
#이때 짝을 이루지 않는 요소를 리턴
#ex: 9,3,9,3,9,7,9 -> [0]=[2] [1]=[3] [4]=[6] [5]=![7]

#테스트 케이스 통과실패
def solution(A):
    answer=0
    for i in A:
        tmp=A.pop(0)
        if tmp in A:
            A.remove(tmp)
    return A

# 변형
def solution(A):
    answer=0
    A=sorted(A)
    while A:
        try:
            a=A.pop()
            b=A.pop()
        except:
            break

        if not a==b:
            break
    return a

A=[9,3,9,3,9,7,9]
print(solution(A))

A1=[1,2,1,2,3]
print(solution(A1))
