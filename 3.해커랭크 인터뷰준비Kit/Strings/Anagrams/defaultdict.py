from collections import defaultdict

def makeAnagram(a,b):
    sum=0
    ddic=defaultdict(int)
    for s in a:
        ddic[s]+=1
    print(ddic)
    for s in b:
        ddic[s]-=1
    print(ddic)
    for x in ddic.values():
        sum=sum+abs(x)
    return sum


a,b=input(),input()
res=makeAnagram(a,b)
print(res)
