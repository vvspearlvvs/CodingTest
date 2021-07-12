def solution(s):
    answer=10000
    for n in range(1,len(s)//2+2):
        print("{}개단위로 짜르기".format(n))
        res=''
        cnt=1
        tmp=s[:n] #단위문자열 초기화

        for i in range(n,len(s)+n,n):
            if tmp == s[i:i+n]:
                cnt+=1
            else:
                if cnt==1:
                    res+=tmp
                else:
                    res+=str(cnt)+tmp
                cnt=1
                tmp=s[i:i+n]
        #print(res)
        answer=min(answer,len(res))
    return answer

#print(solution("a"))
print(solution("aabbaccc"))
#print(solution("abcabcdede"))
#print(solution("abcabcabcabcdededededede"))
#print(solution("xababcdcdababcdcd"))
