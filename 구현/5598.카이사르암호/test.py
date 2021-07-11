original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
revised = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
string = input()

for i in string:
    print(original[revised.index(i)], end ='') #위치로 찾아줌
print(string)
