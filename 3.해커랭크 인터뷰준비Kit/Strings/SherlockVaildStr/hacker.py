#모든 문자가 동일한 횟수로 나타나면 YES
#딱 1번만 제거해서 모든문자가 동일한 횟수로 나타나면 YES
#그 외에 NO

from collections import Counter
def isValid(s):
    check=CouWnter(s) #문자열:등장한횟수
    print(check) #Counter({'a': 4, 'b': 2, 'c': 2})
    count=Counter(check.values()) #문자열횟수:등장한횟수
    print(count) #Counter({2: 2, 4: 1})

    #모든문자열의 개수가 같은 경우 : count key가 한개
    if len(count.keys())==1:
        return "YES"
    #모든문자열의 개수가 다른게 있을 경우
    if len(count.keys())==2:
        max_count=max(count.keys())
        min_count=min(count.keys())
        print(max_count,min_count)

        if max_count-min_count == 1:
            if count[max_count] ==1:
                print("한개만 지우면 되는 경우 ex: aaabbcc")
                return "YES"
        if count[min_count] ==1:
            print("한번만 나온게 있을 ex: aabbc")
            return "YES"
    return "NO"

s = "aaabbcc"
result = isValid(s)
print(result)

#aabbccddeefghi: NO
#abcdefghhgfedecba : YES
#aaaabbcc : NO
