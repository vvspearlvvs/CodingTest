
global answer
def dfs(begin, target, words,visited):

    answer=0
    stacks=[begin]

    while stacks:
        print("visited",visited)
        stack=stacks.pop()
        print("stack",stack)
        if stack == target:
            return answer

        for i in range(len(words)):
            #비교문자열
            tmp=words[i]
            print("tmp",tmp)

            #알파벳다른개수 count
            cnt=0
            for j in range(len(tmp)):
                print(stack[j],tmp[j])
                if stack[j]!=tmp[j]:
                    cnt+=1
            print("다른개수",cnt)

            #딱 한개만 다른경우->단어변환->이동
            if cnt==1:
                visited[i]=1
                stacks.append(words[i])
                print("이동")
        #다 찾고 이동하고 나면 정답횟수+1
        answer+=1
    return answer

def solution(begin, target, words):

    if target not in words:
        return 0
    visited =[0 for i in words] #방문횟수 초기화
    answer = dfs(begin, target, words,visited)
    return answer

begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
