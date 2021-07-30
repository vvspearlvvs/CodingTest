from collections import defaultdict

def solution(tickets):
    answer=[]
    routes=defaultdict(list) #{시작지점:[도착지점]}

    for ticket in tickets:
        start=ticket[0]
        end=ticket[1]
        routes[start].append(end)
    print(routes) #list: {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}

    #도착지점이 2개이상일 경우, 알파벳순서가 앞서는 순서가 되기 위해
    for key in routes.keys():
        routes[key].sort(reverse=True)
    print(routes) #list: {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}

    stack=["ICN"] #항상 인천에서 출발
    while stack:
        print("stack",stack)
        tmp=stack[-1]
        print("stack top",tmp)

        if not routes[tmp]: #끝까지 탐색해서 도착지접이 없을 경우
            answer.append(stack.pop()) #도착한 순서대로 answer에 넣음
        else: #도착지점->시작지점 이어지면, 다음도착지점 stack에 넣음
            stack.append(routes[tmp].pop())
    print(answer)
    answer.reverse() #탐색하는 순서는 도착한순서랑 반대
    return answer

test1=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(test1))

test2=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(test2))
