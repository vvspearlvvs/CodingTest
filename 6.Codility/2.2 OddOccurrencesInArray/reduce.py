from functools import reduce
# reduce : 여러 개의 데이터를 대상으로 주로 누적 집계.
# reduce(집계 함수, 순회 가능한 데이터, 초기값)
# 초기값을 기준으로 데이터를 루프 돌면서 집계 함수를 계속해서 적용하면서 데이터를 누적하는 방식

# 예시list
users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M', 'age': 73},
{'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F', 'age': 29},
{'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M', 'age': 51},
{'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F', 'age': 32},
{'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F', 'age': 42}]

#나이합
user_age_sum = reduce(lambda acc, cur: acc + cur["age"], users, 0)
print(user_age_sum)

#이메일목록
user_email =  reduce(lambda acc, cur: acc + [cur["mail"]], users, [])
print(user_email)

#성별로 분류하기
def names_by_sex(acc, cur):
    sex = cur["sex"]
    if sex not in acc:
        acc[sex] = []
    acc[sex].append(cur["name"])
    return acc

user_sex = reduce(names_by_sex, users, {})
print(user_sex)
