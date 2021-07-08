import sys
input=sys.stdin.readline
T=int(input())

def frequency(word):
    dict={}

    for w in word:
        if w not in dict:
            dict[w]=1
        else:
            dict[w]=dict[w]+1
    #dict=sorted(dict.items(),key=(lambda x:x[1]),reverse=True)
    return dict

def check(dict):
    result=[]
    answer=''
    max=0
    for k, v in fre.items():
        if max<v:
            max=v
    #print(max)
    for k, v in fre.items():
        if v==max:
            result.append(k)
    #print(result)
    if len(result)>=2:
        answer="?"
    else:
        answer=''.join(result)
    return answer

for t in range(T):
    word=input().rstrip()
    fre=frequency(word)
    print(fre)
    print(check(fre))
