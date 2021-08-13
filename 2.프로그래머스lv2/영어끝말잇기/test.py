#포기 : 아 조건은 맞았는데 답을 구하는 방식이 잘못댐 너무 돌아감

from collections import defaultdict
def solution(n, words):
    result=defaultdict(list)
    #탈락되는경우 : words안에 있을경우, 이전단어의끝이랑, 현재단어의 시작이 다를떄
    #탈락자가 누군지
    #탈락자가 몇번째로 말한 단어 인지
    answer=[]
    for num in range(n):
        for index in range(len(words)): #6번비교
            #이미 나온단어일경우
            if (index)%n==num:
                result[num].append(words[index])
                if words[index] in words[:index]:
                    subindex=result[num].index(words[index])
                    print("이미나온단어",words[index],num+1,subindex+1)
    print(result)

    for index in range(1,len(words)-1):
        if words[index-1][-1] != words[index][0]:
            print("끝말잇기 잘못한 단어",words[index])



    return answer

n=3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))

n2=5
words2=["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(n2, words2))

n3=2
words3=	["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n3, words3))
