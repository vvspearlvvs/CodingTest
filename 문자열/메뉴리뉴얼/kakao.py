#메뉴구성
#메뉴구성을 가지고 코스요리 경우 리턴(오름차순)
from itertools import combinations
from collections import Counter

orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course=[2,3,4]
def solution(orders,course):
    answer=[]
    for c in course:#c개 코스
        #c개로 뽑을 수 있는 메뉴조합
        order_combi=[]
        for order in orders:
            for combi in combinations(order,c):
                order_combi.append(''.join(sorted(combi)))
        print(str(c)+"개 코스")
        print(order_combi)
        #['AB', 'AC', 'AF', 'AG', 'BC', 'BF', 'BG', 'CF', 'CG'

        #메뉴구성후보
        order_count=Counter(order_combi).most_common()
        print(order_count)
        #메뉴조합,찾은횟수
        #[('AC', 4), ('CD', 3), ('CE', 3), ('DE', 3),

        #count가 가장 큰거만 result
        #count의 max 구하고
        max=0
        for oc in order_count:
            if oc[1]>=max:
                max=oc[1]
        #max에 해당하는 메뉴구성 추출
        #단 메뉴구성이1개일 경우 제외
        for oc in order_count:
            if oc[1]>=max and oc[1]!=1:
                answer.append(oc[0])
    return sorted(answer)



print(solution(orders,course))
