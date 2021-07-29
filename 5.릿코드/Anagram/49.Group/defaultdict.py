#애너그램끼리 그룹화해라
#애너그램인지 확인하기 위해 단어의 문자를 정렬=key

from collections import defaultdict
def groupAnagrams(strs):
    sorted_list=[]
    anagrams=defaultdict(list)

    for word in strs:
        key=''.join(sorted(word)) #애너그램인지 확인하기 위한 key
        anagrams[key].append(word)
    #print(anagrams)
    return anagrams.values()




strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
