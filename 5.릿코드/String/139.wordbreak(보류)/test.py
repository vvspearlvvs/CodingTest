#wrong : word단위로 나눠서 확인하는게 아니라서 다 True

def workbreak(str,worddict):
    answer=[]
    for word in worddict:
        print(word)
        if word in str:
             answer.append(True)
        else:
            answer.append(False)
    return answer

str1 ="catsandog"
wordDict1=["cats","dog","sand","and","cat"]

str2 = "applepenapple"
wordDict2 = ["apple","pen"]
print(workbreak(str1,wordDict1))
