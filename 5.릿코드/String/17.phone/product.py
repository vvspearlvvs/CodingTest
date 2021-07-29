from itertools import product
def letterCombinations(digits):
    answer=[]
    if digits == "":
        return answer

    letters='abcdefghijklmnopqrstuvwxyz'
    phone=[]
    for i in range(1,6):
        phone.append(letters[(i-1)*3:i*3])
    phone.append(letters[15:19])
    phone.append(letters[19:22])
    phone.append(letters[22:26])

    num =[str(i) for i in range(2,10)]
    phone_num=dict(zip(num,phone))
    print(phone_num)

    items=[]
    for i in digits:
        items.append(list(phone_num[i]))
    print(items)

    product_list=list(product(*items))
    print(product_list)

    #예쁘게
    for item in product_list:
        answer.append(''.join(item))
    return answer
print(letterCombinations("23"))


#product : 두개이상의 리스트에서 모든 조합구하기
#items=[['a', 'b', 'c'], ['d', 'e', 'f']]
#product_list=[('a', 'd'), ('a', 'e'), ('a', 'f'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
#예쁘게 = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
#참고 :combi/permut/product https://velog.io/@davkim1030/Python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-product-itertools
