from collections import defaultdict
from itertools import groupby

def solution(genres, plays):

    music=list(zip(genres, plays))
    print(music) #[('classic', 500), ('pop', 600), ('classic', 150), ('classic', 800), ('pop', 2500)]

    music.sort(key=lambda x:x[0])
    print(music) #[('classic', 500), ('classic', 150), ('classic', 800), ('pop', 600), ('pop', 2500)]

    #groupby할때 묶을기준(genres)으로 정렬이 되어 있어야
    group=groupby(music,lambda x:x[0])


    for k, g in group:
        dict=defaultdict(list)
        dict[k]=list(g)
        print(dict)
        #{'classic': [('classic', 500), ('classic', 150), ('classic', 800)]})
        #{'pop': [('pop', 600), ('pop', 2500)]})

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
print(solution(genres, plays))


#groupby참고 https://wikidocs.net/108940
