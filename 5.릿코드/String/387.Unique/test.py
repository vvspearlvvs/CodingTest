#반복되지 않는 첫번째 문자열의 위치 출력

from collections import Counter
def firstUniqChar(str):
    answer =-1
    count=Counter(str)
    #print(count)
    for i in str:
        if count[i]<=1:
            answer=str.index(i)
            break
    return answer



print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))
