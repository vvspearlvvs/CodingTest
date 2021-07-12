#요구사항
#쌍이 몇개 있는지
#10 20 20 10 10 30 50 10 20 일떄
# (10,10), (10,10),(20,20) 으로 3개

def sockMerchant(n, ar):
    count_dict={}
    for key in set(ar):
        count_dict[key]=ar.count(key)
    #print(count_dict)
    result=0
    for values in count_dict.values():
        if values>=2:
            result=result+values//2
    return result

n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)
