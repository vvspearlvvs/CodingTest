from collections import defaultdict
from collections import Counter

def solution(info, query):
    answer = []
    info_dict=defaultdict(list)

    for i in range(len(info)):
        row=info[i].split()
        info_dict['언어'].append(row[0])
        info_dict['직군'].append(row[1])
        info_dict['경력'].append(row[2])
        info_dict['소울푸드'].append(row[3])
        info_dict['점수'].append(row[4])
    print(info_dict)

    for q in query:
        qrow = q.split()

        #print(type(info_dict['점수'])) #list
        #print(type(qrow[7]))
        #if qrow[0] in info_dict['언어'] and qrow[2] in info_dict['직군'] and qrow[4] in info_dict['경력'] and qrow[6] in info_dict['소울푸드'] and int(info_dict['점수'])>=int(qrow[7]):
        print(qrow[0])
        print(info_dict['언어'])
        for i in range(5):
            if info_dict['언어'][i]==qrow[0] and info_dict['직군'][i]==qrow[2] and info_dict['경력'][i]==qrow[4] and info_dict['소울푸드'][i]==qrow[6] and info_dict['점수'][i]>=qrow[7]:
                print(i)
        #if qrow[0]!='-':
        #    answer.append(info_dict['언어'].index(qrow[0]))
        #else:
        #    answer.append(5)
        #qrow[0]:java,python,-
        #row[2]:back,frontend,-
        #row[4]:senior,junior
        #row[6]:pizza,chicken
        #row[7]:score
    return answer

info = ["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

query=["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]

print(solution(info, query))
#[언어:{java:{0,4},python:{2,3,5},cpp:{}},
