def solution(answers):
    sol1 = [1,2,3,4,5]
    sol2 = [2,1,2,3,2,4,2,5]
    sol3 = [3,3,1,1,2,2,4,4,5,5]
    counts = [0,0,0]
    winner = []
    for index,answer in enumerate(answers):
        if answer == sol1[index%len(sol1)]:
            counts[0]+=1
        if answer == sol2[index%len(sol2)]:
            counts[1]+=1
        if answer == sol3[index%len(sol3)]:
            counts[2]+=1

    for i,s in enumerate(counts):
        if max(counts)==s:
            winner.append(i+1)

    return winner

print(solution([1,2,3,4,5])) #[1]
#print(solution([1,3,2,4,2])) #[1,2,3]

'''
새로알게 된 것
enumerate함수
순서가 있는 자료형을 받아서 인덱스값까지 전달함

'''
