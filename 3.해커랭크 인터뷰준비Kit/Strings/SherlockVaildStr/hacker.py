from collections import Counter

def isValid(s):
    check=Counter(s)
    print(check)
    count=Counter(check.values())
    print(count)

    #모든문자열의 개수가 같은 경우
    if len(count.keys())==1:
        return "YES"
    #모든문자열의 개수가 다른게 있을 경우
    if len(count.keys())==2:
        max_count=max(count.keys())
        min_count=min(count.keys())
        #한개만 지우면 되는 경우
        if max_count-min_count == 1:
            if count[max_count] ==1:
                return "YES"
        if count[min_count] ==1:
            return "YES"
    return "NO"

s = input()
result = isValid(s)
print(result)

#aabbccddeefghi: NO
#abcdefghhgfedecba : YES
#aaaabbcc : NO
