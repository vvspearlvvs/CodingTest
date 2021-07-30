from collections import Counter
def solution(phone_book):
    count=Counter(phone_book)
    #print(count)
    for phone_number in phone_book:
        tmp=""
        for number in phone_number:
            tmp+=number
            #접두어이거나, 자기자신이 아닐경우
            if tmp in count.keys() and tmp !=phone_number:
                return False
    return True



test1=["119", "97674223", "1195524421"]
test2=["123","456","789"]
test3=["12","123","1235","567","88"]
print(solution(test3))
