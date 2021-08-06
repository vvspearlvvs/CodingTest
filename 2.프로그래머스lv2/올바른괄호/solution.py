def solution(s):
    stack=[]
    for item in s:
        if item =='(':
            stack.append(item)
        else:
            if len(stack) ==0:
                return False
            else:
                stack.pop()

    if len(stack)==0:
        return True
    else:
        return False

print(solution("()()"))
