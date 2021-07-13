def solution(s):
    word=['zero','one','two','three','four','five','six','seven','eight','nine']
    dict={}
    result=''
    for i in range(len(word)):
        dict[word[i]]=i
    #print(dict)

    for i in s:
        if i.isalpha():
            tmp+=i
            if tmp in dict.keys():
                result=result+str(dict[tmp])
        else:
            result=result+i
            tmp=''
    print(result)


solution("23four5six7")
