from functools import cmp_to_key

def compare(x,y):
    #x[0]:고유번호 x[1]:재생횟수
    if x[1] == y[1]: #장르내에서 재생횟수가 같다면
        if x[0] < y[0] : #정렬기준3.고유번호가 낮은노래순서로
            return -1 #고유번호가 작은값(x[0])을 앞으로 보낸다.
        else:
            return 1
    elif x[1] < y[1]: #장르내에서 재생횟수가 같지않을땐
        return 1 #정렬기준2.장르 내에서 많이 재생된 노래순서
    else:
        return -1

def solution(genres, plays):
    answer=[]
    score={}
    index={}

    for i,(genre,play) in enumerate(zip(genres,plays)):
        if genre not in score.keys():
            score[genre]=play
            index[genre]=[[i,play]]
        else:
            #print([i, play])
            score[genre]+=play
            index[genre].append([i, play])
    print(score) #{'classic': 1450, 'pop': 3100}
    print(index) #{'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]}

    #정렬기준1.속한 노래가 많이 재생된 장르순서
    top_genre=sorted(score.items(),key=lambda x:x[1],reverse=True)
    print(top_genre) #[('pop', 3100), ('classic', 1450)]

    for genre in top_genre:
        sort_genre=genre[0]
        #정렬기준2.장르 내에서 많이 재생된 노래순서
        sort_music_list=sorted(index[sort_genre],key=cmp_to_key(compare))
        print(sort_music_list)

        #정답:두개씩 모은 베스트앨범 고유번호순서
        for best_music in sort_music_list[:2]:
            best_index = best_music[0]
            answer.append(best_index)
    return answer

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
print(solution(genres, plays))
