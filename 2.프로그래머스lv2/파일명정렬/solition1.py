from collections import defaultdict

def solution(files):
    tmp = []
    filedict=defaultdict(list)
    HEAD, NUM, TAIL = '', '', ''

    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():     # 숫자가 나오면 그 이전은 무조건 HEAD, 이후는 NUMBER, TAIL로 다시 구분
                HEAD = file[:i]
                NUM = file[i:]
                #print(HEAD,NUM)
                for j in range(len(NUM)):    # NUMBER와 TAIL 구분 (숫자 안나오면 TAIL)
                    if not NUM[j].isdigit():
                        TAIL = NUM[j:]
                        NUM = NUM[:j]
                        break
                #print(HEAD,NUM,TAIL)

                filedict[file].append(files.index(file)) #들어온순서대로
                filedict[file].append(HEAD.lower()) #대소문자구분하지 않음
                filedict[file].append(int(NUM)) #01과 1은 정렬시 같은 값으로 처리
                filedict[file].append(TAIL)
                HEAD, NUM, TAIL = '', '', ''
                break

    #print(filedict)
    sortdict=sorted(filedict.items(),key=lambda x:(x[1][1],x[1][2],x[1][0])) #HEAD기준 사전순

    return [''.join(i[0]) for i in sortdict]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))

files3=["foo010bar020.zip"] #foo, 010, bar020.zip
print(solution(files3))
