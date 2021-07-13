#투포인터 방법
#dict사용 : {보석종류:들어온횟수}
#투포인터를 들어온횟수를 직접 count하는게 아니라 인덱스로 count한다.
def solution(gems):
        answer=[1,len(gems)] #답이 될 수 있는 후보
        group=set(gems)
        n=len(group) #종류의 수
        #print("종류",group) #종류
        #print("종류의수",n)
        if len(group) ==1: #예외.보석종류가 한개일경우
            return [1,1]
        dict={} #모든종류별로 담았는지 확인목적
        left=0
        right=1
        standard=gems[left] #보석종류가 다 있는지 비교
        dict[standard]=left #왼쪽에 있는거 넣고
        print("초기화 dict",dict)

        while right<len(gems):
            print("left",gems[left])
            print("right",gems[right])
            print("standard",standard)

            dict[gems[right]] = right #오른쪽에 있는거 넣고
            print("오른쪽에 있는거 넣은 dict",dict)
            #중복된게 또 들어오면 ex : "DIA", "RUBY", "RUBY", "DIA"
            if standard == gems[right]:
                print("중복된게 또 들어오면?",standard," ",gems[right])
                new_sort=sorted(dict.keys(), key=lambda x : dict[x])
                print(new_sort)
                new=new_sort[0]
                print("다음으로 시작할 보석",new)
                standard=new #다음으로 비교할 기준
                left=dict[new] #최근에 담은 보석부터 시작
                print("왼쪽 이동",left)

            if len(dict.keys()) == n : #모든종류
                print("모든종류!")
                if answer[1]-answer[0] > right-left :
                     answer = [left+1, right+1]

            right=right+1 #오른쪽으로 이동
            print("오른쪽 이동",right)
        return answer


gems =["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
res=solution(gems)
print("######")
print(res)
gems3=["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
res=solution(gems3)
print("######")
print(res)
