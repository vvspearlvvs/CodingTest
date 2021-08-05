def solution(s):
    stack=[i for i in s]
    print(stack)
    while stack:
        if stack.pop()==')' and stack[-1]=='(':
            stack.pop()
        elif stack.pop()=='(' and stack[-1]==')':
            stack.pop()
    print("stack",stack)

    if stack is None:
        return "true"
    else:
        return "false"

print(solution("()())"))
