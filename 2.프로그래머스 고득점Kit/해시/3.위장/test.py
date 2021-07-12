def solution(clothes):
    answer = 1
    dict={}
    for list in clothes:
        key= list[1]
        value =list[0]
        if key in dict:
            dict[key].append(value)
        else:
            dict[key]=[value]

    for key in dict.keys():
        answer = answer*(len(dict[key])+1)

    return answer-1


test1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
#test2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(test1))
#print(solution(test2))
