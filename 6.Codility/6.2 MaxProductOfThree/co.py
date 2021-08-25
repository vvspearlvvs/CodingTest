#triplet (P,Q,R) :  A[P] * A[Q] * A[R]
#(0 ≤ P < Q < R < len(A))
#임의의 세 수를 선택했을때 triplet의 최대값

# 양수들끼리의 최대값, 음수2개랑 양수끼리기 롭
def solution(A):
    A.sort() #[-3, -2, 1, 2, 5, 6]
    tmp1 = A[-1] * A[-2] *A[-3] #양수들끼리
    tmp2 = A[0] * A[1] * A[-1] #가장큰 음수2개랑 가장큰 양수
    return max(tmp1,tmp2)

A=[-3,1,2,-2,5,6]
print(solution(A))
