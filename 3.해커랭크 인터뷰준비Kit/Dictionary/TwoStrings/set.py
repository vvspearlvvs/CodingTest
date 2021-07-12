from collections import defaultdict

def twoStrings(s1, s2):
    print(set(s1)) #알파벳 구성
    print(set(s2))
    print(set(s1)&set(s2)) #공통으로 나온 알파벳
    if set(s1)&set(s2):
        return "YES"
    else:
        return "NO"


#q = int(input().strip())
#for q_itr in range(q):
s1 = input()
s2 = input()
result = twoStrings(s1, s2)
