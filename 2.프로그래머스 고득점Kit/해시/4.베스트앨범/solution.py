def solution(genres, plays):
    answer = []

    index = {}
    score = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in index:
            index[genre] = [(i, play)]
        else:
            index[genre].append((i, play))

        if genre not in score:
            score[genre] = play
        else:
            score[genre] += play

    for (k, v) in sorted(score.items(), key=lambda x:x[1], reverse=True):
        for (i, play) in sorted(index[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
print(solution(genres, plays))
