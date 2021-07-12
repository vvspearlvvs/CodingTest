#모든문자가 동일한 횟수만큼 나타나야 유효한 숫자.
#딱 한개의 문자만 제거하고 나서 동일한 횟수만큼 나타나도 유효
#문자열이 유효한지 Y/N
#ex : aabbcd -> a:2,b:2,c:1,d:1
# -> 각각 갯수가 달라서 remove
# case1.각각 개수를 2로 맞추려고 remove = aabb
# case2.각각 개수를 1로 맞추려고 remove = abcd


def isValid(s):
    check={} #'알파벳':'나온숫자'
    count={} #'나온숫자':'나온숫자만큼 몇개있는지'
    for letter in s:
        check[letter]=check.get(letter,0)+1
    print(check)
    for v in check.values():
        count[v]=count.get(v,0)+1
    print(count)

    subb=list(set(check.values()))
    print(subb)
    a=subb[0]
    b=subb[1]
    sub=abs(a-b)
    #1만
    if len(set(check.values()))>2 or sub>1:
        return "NO"
    else:
        return "YES"

s = input()
result = isValid(s)
print(result)
#aabbccddeefghi: NO
#abcdefghhgfedecba : YES
#aaaabbcc : NO
