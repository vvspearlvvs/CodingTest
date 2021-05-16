def solution(phone_book):
    answer = True
    phone_book.sort()
    print(phone_book)
    print(phone_book[1:])
    for p1,p2 in zip(phone_book,phone_book[1:]):
        if p2.startswith(p1):
            answer=False
    return answer

print(solution(["119", "97674223", "1195524421"])) #false
#print(solution(["123","456","789"])) #false
#print(solution(["12","123","1235","567","88"])) #false

'''
새로배운것
startswith
'''
