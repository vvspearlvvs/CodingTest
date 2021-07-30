def solution(begin, target, words):
    answer=0
    stacks=[begin]

    if target not in words:
        return 0

    while len(words)!=0: #wordㅇ의 단어 다 확인할때까지 반복
        sub=[]
        for stack in stacks: #stack원소개수만큼 반복
            for tmp in words: #비교할문자

                #알파벳다른개수 count
                cnt=0
                for j in range(len(stack)):
                    if stack[j]!=tmp[j]:
                        cnt+=1

                #딱 한개만 다른경우->단어변환->이동
                if cnt==1:
                    sub.append(tmp)
                    words.remove(tmp)
        answer+=1
        #반복하기 위해 다시 
        if target in sub:
            return answer
        else:
            stacks =sub

    return answer

begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
