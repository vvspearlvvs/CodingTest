#문제이름:Special String Again
#팰린드롬 개수 구하기 (각 인덱스에 있는 문자마다 다른값으로 봄)
from itertools import groupby

def substrCount(n, str):
    #1개일때, 2개일때, 3개일때 등등 group
    group_list=[]
    for k, g in groupby(str):
        item=(k,len(list(g)))
        group_list.append(item)
    print(group_list) #[('m', 1), ('n', 1), ('o', 1), ('n', 1), ('o', 1), ('p', 1), ('o', 2)]

    count=0
    #문자 하나로 이루어진 팰린드롬
        #ex:aaa일때 6개 (a,a,a,aa,aa,aaa) => 3+2+1
        #ex:bb일때 (b,b,bb) =>2+1
    for i in group_list:
        n=i[1]
        count+=(n*(n+1))//2
    print("문자 하나로 이루어진 팰린드롬",count) #단순히 문자열길이와 같지 않음!!

    #여러문자열로 이루어진 팰린드롬
        #슬라이딩윈도우(start=i-1, end=i+1)
        #start값 end값이 같아야 팰린드롬
    for i in range(1,len(group_list)-1):
        start=i-1
        end=i+1
        #팰린드롬:양끝이 같고 and 가운데는 1번나옴
        if (group_list[start][0] == group_list[end][0]) and group_list[i][1]==1:
            print("팰린드롬")
            start_cnt=group_list[start][1] #여기 이해가안댐
            end_cnt=group_list[end][1]
            count+=min(start_cnt,end_cnt)
    print("여러문자로 이루어진 팰린드롬", count)
    return count

#참고 https://inputting.tistory.com/58


n1= 8
str1 = "mnonopoo"
result = substrCount(n1, str1)
#12 :m,n,o,n,o,p,o,o,non,ono,opo

n2=5
str2="asasd"
result = substrCount(n2, str2)
#7: a,s,a,s,d,asa,asa

n3=7
str3="abcbaba"
result = substrCount(n3, str3) #10
#10 : a,b,c,b,a,b,a,bcb,bab,aba

n4=4
str4="aaaa"
result = substrCount(n4, str4)
#10 : a,a,a,a,aa,aa,aa,aaa,aaa,aaaa
