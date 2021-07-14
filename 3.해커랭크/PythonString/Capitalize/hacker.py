def solve(s):
    result=[]
    split=s.split()
    print(split)
    for word in split:
        if len(word)==1:
            result.append(word.upper())
        else:
            new_word=word[0].upper()+word[1::]
            result.append(new_word)
    return ' '.join(result)

s="chris ala"
result=solve(s)
print(result)
