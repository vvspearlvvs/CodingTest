'''
#2941.크로아티아 알파벳
import sys
input=sys.stdin.readline
str=input().rstrip()
cro_alpha=['c=','c-','dz=','d-','lj','nj','s=','z=']

for cro in cro_alpha:
    str=str.replace(cro,'*')
#print(str)
print(len(str))

#rstrip() : 뒤에 줄바꿈 \n 제거해줌
'''

#1316.그룹단어체커
import sys
input = sys.stdin.readline
n=int(input())
group=0
for _ in range(n):
    str=input()
    error=0
    for i in range(len(str)-1):
        if str[i]!=str[i+1]:
            new_word=str[i+1:]
            #print(new_word)
            if new_word.count(str[i])>0:
                error+=1
    if error ==0:
        group +=1
print(group)
