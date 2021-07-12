#두개의 문장(magazine, note), 단어들이 같은지 비교 (대소문자구분)
#ex:magazine="attack at dawn", note=""Attack at dawn" -> NO
from collections import defaultdict

def checkMagazine(magazine, note):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word]+=1
    for word in note:
        if dicty[word]==0 :
            return False
        dicty[word]-=1
    return True
#6 5
#two times three is not four
#two times three is four

first_multiple_input = input().rstrip().split()
m = int(first_multiple_input[0])
n = int(first_multiple_input[1])
magazine = input().rstrip().split()
note = input().rstrip().split()
res=checkMagazine(magazine, note)
print(res)
