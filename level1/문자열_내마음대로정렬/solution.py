def solution(strings, n):
    answer =[]
    dict={}
    strings.sort() #일단먼저 정렬해 둔 상태에서 시작하
    for word in strings:
        dict[word]=word[n]
    #dict : {'bed': 'e', 'car': 'a', 'sun': 'u'}
    sort_dict=sorted(dict.items(),key=lambda item: item[1]) #value기준정렬
    #sort_dict(type:list) : [('car', 'a'), ('bed', 'e'), ('sun', 'u')
    for k,v in sort_dict:
        answer.append(k) #결과값 key

    return answer



#print(solution(["sun", "bed", "car"],1))
#print(solution(["abce", "abcd", "cdx"],2))

'''
새로알게 된 것
dict 정렬하기 https://codechacha.com/ko/python-sorting-dict/
lambda sort https://stackoverflow.com/questions/13669252/what-is-key-lambda
'''
