#문자열s, 정수k가 주어졌을때
#어떤 문자열을 최대k번 바꾼다.
#그 결과 연속적인 문자가 나타난 가장긴 substring의 길이 구하시오
from collections import Counter
def characterReplacement(s,k):
    start,end=0,0
    max_len=0
    count=Counter()
    for end in range(1,len(s)+1):
        print(end,start)
        count[s[end-1]]+=1
        #print(count) #하나씩 슬라이딩윈도우 추가

        most = count.most_common(1) #최빈값1개 : [('A', 2)]
        print(most)
        most = most[0][1] #최빈값 : 2 => 안바꿔도 되는 문자개수
        remain = (end-start)-most  #슬라이딩 윈도우안에서 남은문자 =>바꿔야하는문자개수

        if remain > k:#바꿔야하는 문자 > 바꿀수있는횟수
            count[s[start]]-=1
            start+=1 #슬라이딩윈도우 크기 줄임
        max_len=max(end-start,max_len)
    return max_len

print(characterReplacement("AABABBA",1))
