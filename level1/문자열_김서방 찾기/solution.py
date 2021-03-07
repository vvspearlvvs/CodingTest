def solution(seoul):
    answer = ''
    for item in seoul:
        if item == "Kim":
            return "kim is in "+str(seoul.index(item))+" here"

list = ["Jane","Kim"]
print(solution(list))
