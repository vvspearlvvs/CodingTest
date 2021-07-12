from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score=score
    def __repr__(self):
        return "{} {}".format(self.name,self.score)
    #커스텀한 기준에는 T/F가 아니라 리턴값 1,0,-1
    def comparator(a, b):
        if a.score == b.score: #점수가 같으면
            if a.name>b.name: #name이 큰 순서대로
                return 1
            else: #name이 작은 순서는 반대
                return -1
        else: #점수가 다르면, 점수가 큰 순서대로
            return b.score-a.score

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

#커스텀한 비교기준을 cmp_to_key에 담아준다
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
