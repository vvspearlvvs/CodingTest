#애나그램: 문자열1을 재배열했을 때 문자열2가 되면 서로 애나그램
#서로 애나그램이 되는 쌍의 개수를 구하시오
#ex : mom -> [m,m],[mo,om] =2개
#ex : abba ->[a,a],[b,b],[ab,ba],[abb,bba] =5개
#ex: abcd -> 없음
from itertools import combinations
from collections import defaultdict

#애나그램이 될 수 있는 모든경우의수 (한글자짜리,두글짜짜리...)
def sherlockAndAnagrams(s):
    total=0
    sub={}

    for i in range(1,len(s)):
        for j in range(len(s)-i+1):
            chunk = ''.join(sorted(s[j:j+1]))
            total+=chunk.setdefault(chunk,0)
            sub[chunk]+=1
    print(total)

    for k,v in sub.items():
        result=result+v*(v-1)//2
    print(result)
sherlockAndAnagrams("abba")

'''
q = int(input().strip())
for q_itr in range(q):
    s = input()
    result = sherlockAndAnagrams(s)
'''
