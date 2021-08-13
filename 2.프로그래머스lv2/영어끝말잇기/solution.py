def solution(n,words):
    answer=[0,0]
    for index in range(len(words)):
        if index!=0:
            if words[index-1][-1] != words[index][0]:
                return [index%n+1,index//n+1]

        if words[index] in words[:index]:
            return [index%n+1,index//n+1]
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
