#아이디어 : a,b를 k로 나누었을때 몫을 구하고,
# A의 나머지가 0이면, B의 몫 - A의 몫 + 1
# A의 나머지가 0보다크면, B의 몫 - A의 몫

def solution(A,B,K):
    QA=A//K #A의 몫
    QB=B//K #B의 몫
    RA=A%K  #A의 나머지
    cnt = QB-QA #B의 몫 - A의 몫
    if RA ==0:
        cnt+=1
    return cnt

print(solution(6,11,2))
