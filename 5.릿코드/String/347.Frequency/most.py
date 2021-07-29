from collections import Counter

def topKFrequent(nums,k):
    answer =[]
    count=Counter(nums)
    #print(count)
    most_list = count.most_common(k)
    for most in most_list:
        answer.append(most[0])
    return answer


nums=[1]
k=1
print(topKFrequent(nums,k))
