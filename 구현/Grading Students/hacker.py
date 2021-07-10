def gradingStudents(grades):
    result=[]
    for grade in grades:
        #print(grade%5)
        #낙제점수이거나 그대로 나오는 경우
        if grade <38 or (grade%5<3):
            score = grade
        #5로 나누었을때, 3이상 남으면 반올림
        else:
            mod_num=grade%5
            round_num = 5-mod_num #나머지
            score=grade+round_num
        result.append(score)
    return result

grades_count = int(input().strip())
grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)
print(result)
