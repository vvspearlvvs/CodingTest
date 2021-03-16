import re

def solution2(s):
    p = re.compile(r'\d(?=\d{4})')
    print(p)
    return p.sub("*", s, count = 0)

print(solution2('01033334444'))

'''
새로배운것 정규식
re.compile
re.sub
'''
