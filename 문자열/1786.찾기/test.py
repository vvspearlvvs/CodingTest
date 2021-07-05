import sys
input = sys.stdin.readline
S = input().rstrip() #ABC ABCDAB ABCDABCDABDE
P = input().rstrip() #ABCDABD

def get_pi(P):
    m = len(P)
    pi = [0 for i in range(m)]
    idx = 0
    for i in range(1, m):
        while idx > 0 and P[i] != P[idx]:
            idx = pi[idx - 1]

        if P[i] == P[idx]:
            idx += 1
            pi[i] = idx

    return pi

n = len(S)
m = len(P)
count=0
result=[] #패턴매칭이 여러번 나타날 수 있으니까 리스트

pi = get_pi(P)
#print(pi)
idx = 0
for i in range(0, n):
    while idx > 0 and S[i] != P[idx]:
        idx = pi[idx - 1]
    if S[i] == P[idx]:
        if idx == m - 1:
            ## 같은패턴을 찾음
            #print("패턴매칭")
            result.append(i-m+2) #패턴이 나타나는 위치
            count+=1 # 패턴매칭이 몇번 나타는지
            idx = pi[idx]
        else:
            idx += 1
print(count)
for i in result:
    print(i,end=" ")
