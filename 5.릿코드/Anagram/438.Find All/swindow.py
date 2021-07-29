from collections import Counter
def findAnagrams(a,b):
    answer=[]
    m,n=len(a),len(b)
    if m<n: #예외사항
        return answer
    bcounter = Counter(b)
    acounter = Counter(a[:n-1]) #n-1만큼 문자열자름(윈도우크기)

    print("애너그램문자열",bcounter) #Counter({'a': 1, 'b': 1})
    print("비교문자열",acounter) #Counter({'a': 1})

    end=0 #윈도우 맨뒤 인덱스
    for end in range(n-1,m):
        start=end-(n-1) #윈도우 맨앞 인덱스
        print(start,end)

        acounter[a[end]]+=1 #슬라이딩윈도우 맨뒤 추가
        print("맨뒤추가",acounter) #즉, a[end]라는 키값의 value를 +1
        if acounter==bcounter: #애너그램등장
            print("맨뒤 추가했더니 애너그램등장",acounter)
            answer.append(start) #정답 : 애너그램 등장한 위치

        acounter[a[start]]-=1 #슬라이딩윈도우 맨앞 빼기
        print("앞삭제",acounter) #즉, a[start]라는 키값의 value를 -1
        if acounter[a[start]] ==0: #실제로 value가 0이 된 key들은 삭제
            print("애너그램이랑 상관없어서 맨앞 삭제")
            del acounter[a[start]]
    return answer

a = "cbaebabacd"
b = "abc"

a1="abab"
b1="ab"
print(findAnagrams(a,b))
