import string
TEMP=string.digits+string.ascii_lowercase
#TEMP = '0123456789abcdefghijklmnopqrstuvwxyz'

def jinbump(number,jin):
    q,r=divmod(number,jin)
    if q==0:
        return TEMP[r]
    else:
        return jinbump(q,jin)+TEMP[r]

def solution(n):
     answer = ''.join(reversed(jinbump(n,3)))
     return int(answer,3)

print(solution(45)) #7
print(solution(125)) #229

'''
새로배운것
10진법으로 변환하기 int(숫자,원래몇진법)
'''
