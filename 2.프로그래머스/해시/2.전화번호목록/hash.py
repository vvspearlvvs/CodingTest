def solution2(phone_book):
    dict={}
    for phone_num in phone_book:
        dict[phone_num] = 1
    print(dict)
    for phone_num in phone_book:
        tmp =""
        for num in phone_num:
            tmp+=num
            print(tmp)
            if tmp in dict and tmp!=phone_num:
                return False
    return True

print(solution2(["119", "97674223", "1195524421"])) #false
#print(solution2(["123","456","789"])) #true
#print(solution2(["12","123","1235","567","88"])) #false
#print(solution2(["123", "456", "12"])) #false
