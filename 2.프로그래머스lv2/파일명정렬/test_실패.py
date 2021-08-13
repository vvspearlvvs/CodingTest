from collections import defaultdict

def solution(files):
    answer = []
    filedict=defaultdict(list)

    #1.분할
    for file in files:
        HEAD=''
        NUM=''
        if "." in file:
            TAIL="."+file.split(".")[-1]
        else:
            TAIL=''

        for f in file.split(".")[0]:
            if f.isdigit():
                NUM=NUM+f
            else:
                HEAD=HEAD+f

        #print(HEAD,NUM,TAIL)
        filedict[file].append(files.index(file)) #들어온순서대로
        filedict[file].append(HEAD.lower()) #대소문자구분하지 않음
        filedict[file].append(int(NUM)) #01과 1은 정렬시 같은 값으로 처리
        filedict[file].append(TAIL)
    #print(filedict)

    #2.정렬
    sortdict=sorted(filedict.items(),key=lambda x:(x[1][1],x[1][2],x[1][0])) #HEAD기준 사전순
    #print(sortdict)

    for i in sortdict:
        answer.append(i[0])

    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))

files2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files2))

#예외사항
files3=["foo010bar020.zip"] #foo, 010, bar020.zip
print(solution(files3))
