from collections import Counter

def solution(clothes):
    answer=1

    #dict만들기
    dict={}
    for clothe in clothes:
        cloth_key=clothe[1]
        cloth_value=clothe[0]

        if cloth_key not in dict.keys():
            dict[cloth_key]=[cloth_value]
        else:
            dict[cloth_key].append(cloth_value)
    print(dict)

    #조합 개수 구하기 -> 직접 조합 구할 필요없음(공식이용)
    for key in dict.keys():
        answer = answer*(len(dict[key])+1)
        #경우의수 : (모자갯수+1) * (안경갯수+1)*(신발갯수+1)
    return answer-1



test0=[["yellowhat", "headgear"],
        ["bluesunglasses", "eyewear"]]
#dict:{'headgear': ['yellowhat'], 'eyewear': ['bluesunglasses']}
#solution(test0)

test1 = [["yellowhat", "headgear"],
        ["bluesunglasses", "eyewear"],
        ["green_turban", "headgear"]]
#dict:{headgear: [yellowhat,green_turban],eyewear:[bluesunglasses]}
print(solution(test1))

test2=[["crowmask", "face"],
        ["bluesunglasses", "face"],
        ["smoky_makeup", "face"]]
#dict:{face: [crowmask,bluesunglasses,smoky_makeup]}
print(solution(test2))

#참고 reduce
https://www.daleseo.com/python-functools-reduce/
