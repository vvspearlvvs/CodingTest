def countLetters(word):
    check={}
    for letter in word:
        if letter in check:
            check[letter]=check[letter]+1
        else:
            check[letter]=1
    print(check) #{'w': 2, 'o': 3 }

def countLetters2(word):
    check={}
    for letter in word:
        check[letter]=check.get(letter,0)+1
    print(check)



word='wowoo'
countLetters(word)
countLetters2(word)
