#시간초과
from itertools import combinations,permutations
def biggerIsGreater(w):
    word=[]
    n=len(w)
    combi=list(permutations(w,n))
    for i in combi:
        answer=''.join(i)
        word.append(answer)
    word.sort()
    print(word)

    k=0
    if w==word[-1]:
        return "no answer"
    else:
        for i,wo in enumerate(word):
            if wo==w:
                k=i+1
        return word[k]

T = int(input().strip())
for T_itr in range(T):
    w = input()
    result = biggerIsGreater(w)
    print(result)
