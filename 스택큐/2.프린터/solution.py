def solution(priorities, location):
    answer = 0
    queue = [(i,p) for i ,p in enumerate(priorities)]
    print(queue)

    while True:
        cur=queue.pop(0)
        print(cur)
        if (any(cur[1]<q[1] for q in queue)):
            queue.append(cur)
        else:
            answer+=1
            if cur[0] == location:
                return answer


print(solution([2, 1, 3, 2],2))
