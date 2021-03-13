def solution(x):
    list_int=list(map(int,str(x))) #[1,0]
    if x%sum(list_int)==0:
        return True
    else:
        return False

print(solution(10)) # true
print(solution(12)) # true
