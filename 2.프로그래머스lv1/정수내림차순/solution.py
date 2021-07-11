def solution(n):
    answer=''
    tmp = sorted(list(map(int,str(n))),reverse=True)
    for i in tmp:
        answer=answer+str(i)
    return int(answer)


print(solution(118372))

'''
괜히 복잡하게 형변환했네
다른풀이
    ls=list(str(n))
    ls.sort(reverse=True)
    return int(''.join(ls))'''
