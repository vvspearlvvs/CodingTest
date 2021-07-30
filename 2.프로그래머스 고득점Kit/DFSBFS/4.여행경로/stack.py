from collections import defaultdict

def solution(tickets):
    answer=[]
    routes=defaultdict(list)

    for ticket in tickets:
        start=ticket[0]
        end=ticket[1]
        routes[start].append(end)
    print(routes) #list: {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}

    #가능한경로가2개일경우, 알파벳순서가 앞서는 순서가 되기 위해
    for key in routes.keys():
        routes[key].sort(reverse=True)
    print(routes) #list: {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}

    stack=["ICN"] #항상 인천에서 출발
    while stack:
        print("stack",stack)
        tmp=stack[-1]
        print("stack top",tmp)
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()
    return answer

test1=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(test1))

test2=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(test2))
