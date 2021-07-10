def camelcase(s):
    alist=[]
    word=''
    k=0
    for i in range(0,len(s)):
        if s[i].islower():
            word=word+s[i]
        elif s[i].isupper():
            alist.append(word)
            word=''
            word=word+s[i]
        print(word)
    print(alist)


s = "saveChangesInTheEditor"
result = camelcase(s)
