from collections import Counter
def makeAnagram(a,b):
    a = Counter(a)
    #Counter({'o': 2, 's': 1, 'h': 1, 'w': 1, 'm': 1, 'a': 1, 'n': 1})
    #print("most comomn")
    #print(a.most_common())
    #print(a.most_common(n=2))
    b = Counter(b)
    #Counter({'w': 1, 'o': 1, 'm': 1, 'a': 1, 'n': 1})
    c = a - b
    #Counter({'s': 1, 'h': 1, 'o': 1})
    d = b - a
    #Counter()
    e = c + d
    #Counter({'s': 1, 'h': 1, 'o': 1})
    print(len(list(e.keys())))

a="shooowwman"
b="woman"
res=makeAnagram(a,b)
