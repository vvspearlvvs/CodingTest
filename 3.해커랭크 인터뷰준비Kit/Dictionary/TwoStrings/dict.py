
def twoStrings(s1, s2):
    result=[]
    dic={}
    for i in s1:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    #print(dic)
    for i in s2:
        if i in dic.keys():
            result.append(i)

    if result:
        return "YES"
    else:
        return "NO"

#q = int(input().strip())
#for q_itr in range(q):
s1 = input()
s2 = input()
result = twoStrings(s1, s2)
print(result)
