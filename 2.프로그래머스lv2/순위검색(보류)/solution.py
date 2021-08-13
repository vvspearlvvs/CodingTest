from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = []
    info_dict=defaultdict(list)
    #{키워드로 만들수 있는 조합 : [그 경우에 해당하는 점수들]}
    #ex : {'java':[80,150],.. 'javapizza':[150].....'-':[전부]}

    #1.info가지고 dict생성
    for i in info:
        row=i.split()
        info_keylist=row[:-1] #그외의 내용 : key가 될 후보
        info_value=int(row[-1]) #점수
        print("1.1 info_keylist",info_keylist," info_value",info_value)

        #1.1 하나의info에 대한 경우의수 16개 = key
        for i in range(5):
            for c in combinations(info_keylist,i):
                #print(c) #1개선택, 2개선택,3개선택,.... 모두다 선택될 경우
                info_key = ''.join(c)
                #print(tmp_key)
                info_dict[info_key].append(info_value) #하나의info에 대한 가능한 경우를 key, 점수를 value

    #1.2 점수값들을 오름차순정렬 (이후 이분탐색을 위해)
    for key in info_dict.keys():
        info_dict[key].sort()
    print()
    print(info_dict)
    print()

    #2.query정리
    for q in query:
        qrow=q.split(' ')
        query_score=int(qrow[-1]) #점수
        query=qrow[:-1] #그외의 내용 : key가 될 후보

        #2.1 query_keylist처리 : and 제거
        for _ in range(3):
            query.remove('and')
        #2.2 query_keylist처리 : - 제거
        while '-' in query:
            query.remove('-')
        query_key = ''.join(query)
        print("2.1 query_key", query_key," query_score",query_score)

        #3.lower bound사용해 query_score 보다 큰 점수들의 개수를 구하기
        #3-1.쿼리에 해당하는 score 찾음
        if query_key in info_dict:
             scoreList = info_dict[query_key] #dict에서 키워드에 해당하는 score 뽑음
             print("3.1 select result", scoreList)
             print()

             #3-2.socre보다 큰 점수들의 개수를 세는 방법 : 이분탐색
             if len(scoreList)>0:
                 start=0
                 end=len(scoreList)
                 while start< end:
                     mid=(start+end) //2
                     if scoreList[mid] >= query_score:
                         end = mid
                     else:
                         start = mid+1
                 answer.append(len(scoreList)-start)

        #3-1.쿼리에 해당하는 score가 없을때
        else:
            answer.append(0)

    return answer








info = ["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

query=["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]

print(solution(info, query))
