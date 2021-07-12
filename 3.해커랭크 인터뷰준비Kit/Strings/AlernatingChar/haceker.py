#A와B로만 이루어진 문자열
#인접한 문자열이 없도록 문자열을 바꾸는 최소의 수?
#ex:AABAAB -> ABAAB->ABAB  : 2
#ex:AAABBB-> AABBB->ABBB->ABB->AB : 5
#ex:AAAA->A :3
#ex:BABA : 9
from collections import deque
def alternatingCharacters(s):
    s=deque(s)
    substr=[]
    cnt=0
    for i in list(s):
        if len(substr)==0 or substr[-1]!=i:
             substr.append(s.popleft())
        elif substr[-1]==i:
             s.popleft()
             cnt+=1
        #print(substr)
    return cnt

print(alternatingCharacters("ABABAB"))
