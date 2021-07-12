#같은substring이 있는지
def twoStrings(s1, s2):
    result=[]
    for i in s1:
        if i in s2:
            result.append(i)
    for i in s2:
        if i in s1:
            result.append(i)
    if set(result):
        print("YES")
    else:
        print("NO")

q = int(input().strip())
for q_itr in range(q):
    s1 = input()
    s2 = input()
    result = twoStrings(s1, s2)
