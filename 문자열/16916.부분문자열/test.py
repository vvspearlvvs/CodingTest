#KMP 알고리즘
import sys
input = sys.stdin.readline
pi = []
str1 = input().rstrip()
str2 = input().rstrip()

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

def kmp(S, P):
    n = len(S)
    m = len(P)

    pi = get_pi(P)
    print(pi)
    idx = 0
    for i in range(0, n):
        while idx > 0 and S[i] != P[idx]:
            idx = pi[idx - 1]
        if S[i] == P[idx]:
            if idx == m - 1:
                #같은패턴을 찾음
                return 1
            else:
                idx += 1
    #같은패턴을 못찾음            
    return 0

#print(kmp(str1, str2))
print(kmp(str1, str2))
'''
## 시간오래걸림 (re사용)
if re.search(p,s):
    print("1")
else:
    print("0")
'''

'''
##시간초과
if P in S:
    print("1")
else:
    print("0")
'''
