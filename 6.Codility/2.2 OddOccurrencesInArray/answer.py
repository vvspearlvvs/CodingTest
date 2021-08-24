from functools import reduce

def solution(A):
    A=sorted(A)
    print(A)

    for i in range(0,len(A),2):
        if i+1 == len(A):
            return A[i]
        if A[i] == A[i+1]:
            return A[i]

#다른풀이 XOR성질을 이용
def solution2(A):
  return reduce(lambda x,y: x^y, A)

A=[9,3,9,3,9,7,9]
print(solution2(A))

A1=[1,2,1,2,3]
print(solution2(A1))
