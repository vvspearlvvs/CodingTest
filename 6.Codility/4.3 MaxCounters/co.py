#if A[K]=X 이면 increate
#if A[K]=N+1 이면 max counter
#[3,4,4,6,1,4,4]

def solution(N,A):
    result=[0]*N
    for i in A:
        if 1<=i<=N:
            result[i-1]+=1
        else:
            result=[max(result)]*N
    return result
