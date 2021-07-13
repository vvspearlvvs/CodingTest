#모든문자가 동일한 횟수만큼 나타나야 유효한 숫자.
#딱 한개의 문자만 제거하고 나서 동일한 횟수만큼 나타나도 유효
#문자열이 유효한지 Y/N
#ex : aabbcd -> a:2,b:2,c:1,d:1
# -> 각각 갯수가 달라서 remove
# case1.각각 개수를 2로 맞추려고 remove = aabb
# case2.각각 개수를 1로 맞추려고 remove = abcd

#반만 맞음
def isValid(s):
    check={} #'알파벳':'나온숫자'
    count={} #'나온숫자':'나온숫자만큼 몇개있는지'
    for letter in s:
        check[letter]=check.get(letter,0)+1
    print(check)
    for v in check.values():
        count[v]=count.get(v,0)+1
    print(count)

    #무슨경우에 YES,NO인지 모르겠다.

    #case1 : aaaaaa
    if len(count.keys())==1:
        return "YES"
    #case2 : aabbccddeee, aabbefg 등등..
    if len(count.keys())==2:
        max_count=max(count.keys())
        min_count=min(count.keys())
        #case2-1 : abcdefghhgfedecba {2:7,3:1} 한번만 삭제하면 유효
        #case2-1 반례 : aabbccddeefghi {2:5,1:4} -> False
        if max_count-min_count ==1:
            if count[max_count]==1:
                return "YES"
        #case2-2: aabbccd {2:3,1:1}가장적은것만 삭제하면 유효
        if count[min_count]==1:
            return "YES"
    return "NO"

s = input()
result = isValid(s)
print(result)
#aabbccddeefghi: NO
#abcdefghhgfedecba : YES
#aaaabbcc : NO
