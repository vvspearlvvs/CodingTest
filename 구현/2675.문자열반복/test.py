#2675.문자열반복
'''
T=int(input())
for _ in range(T):
    a,str=input().split()
    for i in str:
        result=i*int(a)
        print(result,end='')
    print()
'''
#1157.단어공부
s=input()
S=list(s.upper())
dict={}
#dict {문자열 : 횟수}
for str in S:
    if str in dict:
        dict[str]+=1
    else:
        dict[str]=1
#print(dict)
#가장 큰 count값 가져오기
max=0
for key, value in dict.items():
    if max<value:
        max=value
#print(max)
#가장 큰 count값이 있는 key(result)가져오기
count=0
for key,value in dict.items():
    if max==value:
        count=count+1
        #print(key,value)
        result=key
#print(count)
#max count값이 2개이상이면 ? 출력, 아니면 그 result
if count>=2:
    print('?')
else:
    print(result)
#1152.단어의 개수
#print(len(input().split()))
