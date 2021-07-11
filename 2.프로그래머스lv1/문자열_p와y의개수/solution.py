def solution(s):
    if s.lower().count('p') == s.lower().count('y'):
        return True
    else:
        return False
        
print(solution("pPoooyY")) # True
print(solution("Pyy")) # False
