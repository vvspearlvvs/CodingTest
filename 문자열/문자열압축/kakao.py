def solution(S):
    print("input:{}".format(S))
    answer = 0
    length=[]
    #n개단위로 짜른 문자열 : n은 len(st//2)까지
    #2부터 하면 안됌. 예외:aabbaccc
    for n in range(1,len(S)//2+1):
        print()
        print("{}개단위로 짜르기".format(n))

        #짜른단위만큼 같은 문자가 몇개 있는지(count X)
        count=1
        result=''
        tmpstr=S[:n]
        #print("초기화")
        #print(tmpstr)
        for i in range(n,len(S),n):
            #print("#비교>>>"+str(i))
            #print(tmpstr,S[i:i+n]) #첫번째, 이후값들

            if S[i:i+n]==tmpstr:
                count=count+1
            else:
                if count==1:
                    count=""
                result+=str(count)+tmpstr
                tmpstr=S[i:i+n]
                count=1
        #print("#최종")
        #print(result)

        #짜르고 남은것들까지 붙인 최종
        if count==1:
            count=""
        result+=str(count)+tmpstr
        #print("한번더")
        #print(result)
        length.append(len(result))
        print(length)
    #print("리턴")
    return min(length)



    '''
    for sb in ssplit:
        count=0
        if sb not in count_dict:
            count=count+1
            count_dict[sb]=count
        else:
            count_dict[sb]=count_dict[sb]+1
    print(count_dict)
    '''


    #새로운 문자열



#"aabbaccc"	7
#"ababcdcdababcdcd"	9
#"abcabcdede"	8
#"abcabcabcabcdededededede"	14
#"xababcdcdababcdcd"	17
#print(solution("aabbaccc"))
#print(solution("ababcdcdababcdcd"))
#print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
#print(solution("xababcdcdababcdcd"))
