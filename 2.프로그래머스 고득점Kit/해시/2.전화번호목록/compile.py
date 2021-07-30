import re #정규식 이용
def solution(phone_book):
    for phone_number in phone_book:
        #complie패턴^ : 이 패턴으로 시작해야함
        tmp = re.compile("^"+phone_number)
        print(tmp)
        for phone_number2 in phone_book:
            if tmp.match(phone_number2) and phone_number!=phone_number2:
                return False
    return True

test3=["12","123","1235","567","88"]
print(solution(test3))
