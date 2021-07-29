def workbreak(str,worddict):
    def canbreak(str,m,worddict):
        if str in m:
            return m[str]
        if str in worddict:
            m[str]=True
            return True

        for i in range(1,len(str)):
            r=str[i:]
            if r in worddict and canbreak(str[0:i],m,worddict):
                m[str]=True
                return True
        m[str]=False
        return False
    return canbreak(str,{},set(worddict))


str1 ="catsandog"
wordDict1=["cats","dog","sand","and","cat"]

str2 = "applepenapple"
wordDict2 = ["apple","pen"]
print(workbreak(str1,wordDict1))
print(workbreak(str2,wordDict2))
